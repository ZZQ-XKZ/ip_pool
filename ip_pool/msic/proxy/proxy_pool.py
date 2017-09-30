import threading
import time
from datetime import datetime
from schedule import Scheduler
from msic import config
from msic.common import utils
from sqlalchemy import create_engine,or_
from sqlalchemy.orm import sessionmaker
from msic import config
from msic.proxy.proxy import Proxy
import concurrent.futures
TASK_INTERVAL = 0
FAILED_COUNT_BORDER = 3
MIN_PROXY_COUNT = 10
lock = threading.Lock()

REDIS_KEY_LAST_CHECK_IP_TIME = "last_check_ip_time"


class ProxyPool(object):
    def __init__(self):
        print("__init__")
        self.engine = create_engine('mysql+mysqldb://'+config.MYSQL_USR+':'+config.MYSQL_PASSWD+'@'+config.MYSQL_HOST+'/'+config.DATABASE_NAME,echo=False)
        Proxy.create_table(self.engine)
        self.session_cls = sessionmaker(bind=self.engine)
        self.session = self.session_cls()
    # Singleton
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            org = super(ProxyPool, cls)
            cls._instance = org.__new__(cls, *args)
        return cls._instance

    def random_choice_proxy(self,bInternal) -> str:
        now_time = utils.get_utc_date()
        available_time = utils.get_utc_time(-60)
        if bInternal:
            proxy = self.session.query(Proxy).filter(Proxy.last_use_time<available_time,Proxy.internal_validity==True,Proxy.internal_response_speed>0).order_by(Proxy.internal_response_speed).first()
        else:
            proxy = self.session.query(Proxy).filter(Proxy.last_use_time<available_time,Proxy.external_validity==True,Proxy.external_response_speed>0).order_by(Proxy.external_response_speed).first()
        proxy.last_use_time= now_time
        proxy.used_count = proxy.used_count + 1
        self.calc_proxy_weight(proxy)
        self.session.commit()
        return proxy.ip

    def calc_proxy_weight(self,proxy):
        if proxy.internal_validity:
            proxy.internal_weight = (1+proxy.failed_count/proxy.used_count)*proxy.internal_response_speed
        if proxy.external_validity:
            proxy.external_weight = (1+proxy.failed_count/proxy.used_count)*proxy.external_response_speed

    def add_failed_time(self,ip):
        print("add_failed_time:"+ip)
        proxy = self.session.query(Proxy).filter(Proxy.ip==ip).first()
        if proxy == None:
            print("can not find ip:"+ip)
            return
        proxy.failed_count = proxy.failed_count + 1
        self.calc_proxy_weight(proxy)
        if proxy.failed_count > FAILED_COUNT_BORDER:
            proxy.internal_validity = False
            proxy.external_validity = False
        
        self.session.commit()


    def crawl_proxy_task(self,proxy_list):
        for proxy in proxy_list:
            count = self.session.query(Proxy).filter(Proxy.ip==proxy.ip).count()
            if count == 0:
                self.session.add(proxy)
        self.session.commit()
        self.last_check_time = datetime.utcnow().timestamp()

    def _thread_check_ip(self,proxy):
        with lock:
            ip = proxy.ip
        start_time = time.time()
        proxy.last_use_time = utils.get_utc_date()
        proxies = { "http": "http://"+ip, "https": "http://"+ip, }   
        try:
            response = utils.http_request('https://google.com', timeout=5,proxies = proxies)
            with lock:
                proxy.external_validity = response.status_code == 200
                proxy.used_count = proxy.used_count + 1
                proxy.external_response_speed = round(time.time() - start_time, 4)*1000
            response.close()
        except (KeyboardInterrupt):
            exit()
        except:
            with lock:
                proxy.external_validity = False
                proxy.external_response_speed = -1
        
        start_time=time.time()
        try:
            response = utils.http_request('https://www.baidu.com',timeout = 5,proxies = proxies)
            with lock:
                proxy.internal_validity=response.status_code==200
                proxy.used_count = proxy.used_count + 1
                proxy.internal_response_speed=round(time.time() - start_time, 4)*1000
            response.close()
        except (KeyboardInterrupt):
            exit()
        except:
            with lock:
                proxy.internal_validity = False
                proxy.internal_response_speed = -1
        with lock:
            utils.log('Check IP:'+ip+' finished i:'+str(proxy.internal_validity)+' e:'+str(proxy.external_validity))
            self.calc_proxy_weight(proxy)
            self.session.commit()
            
    def _check_ip_availability_task(self,proxy_list):
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            future_to_proxy = {executor.submit(self._thread_check_ip,proxy):proxy for proxy in proxy_list}
            for rt in concurrent.futures.as_completed(future_to_proxy):
                print("thread complete")
                
    def check_ip_availability_by_range(self,begin,end):
        proxy_list=self.session.query(Proxy)[begin:end]
        self._check_ip_availability_task(proxy_list)
            
    def check_ip_availability_task(self,time):
        need_update_date=utils.get_utc_date(-time)
        proxy_list=self.session.query(Proxy).filter(Proxy.last_use_time<need_update_date).all()
        utils.log('Start check count:'+str(len(proxy_list)))
        self._check_ip_availability_task(proxy_list)
        
    def check_all_ip_availability_task(self):
        count = self.get_ip_count()
        self.check_ip_availability_by_range(0,count)

    def check_new_ip_availability_task(self):
        proxy_list = self.session.query(Proxy).filter(Proxy.internal_validity==True,Proxy.internal_response_speed==-1,Proxy.external_validity==True,Proxy.external_response_speed==-1).all()
        self._check_ip_availability_task(proxy_list)
        
    def get_ip_count(self):
        return self.session.query(Proxy).count();
proxy_pool = ProxyPool()
