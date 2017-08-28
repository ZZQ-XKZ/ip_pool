import threading
import time
from datetime import datetime

from schedule import Scheduler

from msic import config
from msic.common import utils
from msic.proxy import proxy_strategy
from msic.core.service import mysql_service

TASK_INTERVAL = 0
FAILED_COUNT_BORDER = 3
MIN_PROXY_COUNT = 10

REDIS_KEY_LAST_CHECK_IP_TIME = "last_check_ip_time"


class ProxyPool(object):
    TABLE_NAME = 'proxy_pool'

    def __init__(self):
        self.collection = mysql_service.get_pool(config.MYSQL_HOST,config.DATABASE_NAME,config.MYSQL_USR,config.MYSQL_PASSWD)

    # Singleton
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            org = super(ProxyPool, cls)
            cls._instance = org.__new__(cls, *args)
        return cls._instance

    def random_choice_proxy(self) -> str:
        now_time = utils.get_utc_time()
        available_time = utils.get_utc_time(-60)
        ip_list = mysql_service.excuate_sql(self.collection,"select ip,failed_count,response_speed from ip_pool where update_time <\"{time}\" order by validity desc,response_speed asc limit 1,10 ;".format(time=available_time))
        min_weight_ip = ip_list[0][0]
        min_weight = 99999
        for ip in ip_list:
            weight = ip[1]*500+ip[2]
            if weight < min_weight:
                min_weight = weight
                min_weight_ip = ip[0]
        mysql_service.excuate_sql(self.collection,"update ip_pool set update_time= \"{now_time}\" where ip=\"{ip}\";".format(now_time = now_time,ip = min_weight_ip))
        return min_weight_ip

    def add_failed_time(self, ip):
        add_failed_time_sql = "update ip_pool set failed_count = failed_count +1 where ip=\"{ip}\";".format(ip=ip)
        mysql_service.excuate_sql(self.collection,add_failed_time_sql)
        failed_count = mysql_service.excuate_sql(self.collection,"select failed_count from ip_pool where ip=\"{ip}\";".format(ip=ip))[0][0]
        if failed_count > FAILED_COUNT_BORDER:
            try:
                mysql_service.excuate_sql(self.collection,"delete from ip_pool where ip ="+ip+";")
            except:
                pass
       # self.crawl_proxy_task()


    def crawl_proxy_task(self,proxy_list):
        print(proxy_list)
        for proxy in proxy_list:
            count = mysql_service.excuate_sql(self.collection,"select count(*) from ip_pool where ip =\""+proxy.ip+"\";" )
            if count[0][0] >0:
                sql = "update ip_pool set update_time = \"{update_time}\",failed_count = {failed_count},response_speed={response_speed},validity = {validity} where ip =\"{ip}\";"
                mysql_service.excuate_sql(self.collection,sql.format(ip=proxy.ip,update_time=proxy.update_time,failed_count=proxy.failed_count,response_speed=proxy.response_speed,validity=proxy.validity))
            else:
                sql = "insert into ip_pool values(\"{ip}\",\"{origin}\",\"{create_time}\",\"{update_time}\",{failed_count},{response_speed},{validity});"
                return_data = mysql_service.excuate_sql(self.collection,sql.format(ip=proxy.ip,origin=proxy.origin,create_time =proxy.create_time,update_time=proxy.update_time,failed_count=proxy.failed_count,response_speed=proxy.response_speed,validity=proxy.validity))
                print(return_data)
        self.last_check_time = datetime.utcnow().timestamp()

    def check_ip_availability_task(self):
        last_check_time = self.last_check_time
        now_time = datetime.utcnow().timestamp()
        if last_check_time is not None and (now_time - float(last_check_time)) < (TASK_INTERVAL * 60):
            return
        self.last_check_time=now_time

        proxy_list = mysql_service.excuate_sql(self.collection,"select * from ip_pool")
        for proxy in proxy_list:
            ip = proxy[0]
            start_time = time.time()
            is_success = True
            try:
                proxies = { "http": "http://"+ip, "https": "http://"+ip, }   

                response = utils.http_request('http://newhouse.sh.fang.com/house/s/', timeout=2,proxies = proxies)
                is_success = response.status_code == 200
                response.close()
            except:
                is_success = False
            if not is_success:
                try:
                    mysql_service.excuate_sql(self.collection,"delete from ip_pool where ip =\""+ip+"\";")
                except:
                    pass
                utils.log('Check ip %s FAILED' % ip)
            else:
                elapsed = round(time.time() - start_time, 4)
                try:
                    mysql_service.excuate_sql(self.collection,"update ip_pool set update_time=\"{update_time}\",response_speed={response_speed},validity={validity} where ip = \"{ip}\";".format(update_time=utils.get_utc_time(),response_speed=elapsed*1000,validity=1,ip=ip))
                except:
                    pass
                utils.log('Check ip %s SUCCESS' % ip)

proxy_pool = ProxyPool()
