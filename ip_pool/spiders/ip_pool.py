# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from msic.proxy.proxy_pool import proxy_pool
from msic.proxy.proxy import Proxy
proxy_list = []
class IPPoolSpider(scrapy.Spider):
    name ="ip_pool"
    start_urls_back =[
        'http://www.kuaidaili.com/proxylist/%d/' %i  for i in range(1,10)
    ]+[
        'http://www.xicidaili.com/nn/'
    ]

    start_urls = ['http://www.xicidaili.com/nn/']
    
    def __init__(self,crawler):
        self.crawler = crawler
        dispatcher.connect(self.close,signals.spider_closed)

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def parse(self,response):
        if response.url.find("kuaidaili")!=-1:
            self.parse_kuaidaili(response)
        elif response.url.find("xicidaili") != -1:
            self.parse_xicidaili(response)

    def parse_xicidaili(self,response):
        for data in response.xpath("//table[@id='ip_list']//tr"):
            if data.xpath("./td"):
                _temp=data.xpath("./td/text()").extract()
                ip= _temp[0]
                port = _temp[1]
                proxy_list.append(Proxy.create(ip+":"+port,"xicidaili"))

    def parse_kuaidaili(self,response):
        for data  in response.xpath("//div[@id='freelist']//tr"):
            ip = data.xpath(".//td[@data-title='IP']/text()").extract_first()
            port = data.xpath(".//td[@data-title='PORT']/text()").extract_first()
            if ip !=None and port !=None:
                proxy_list.append(Proxy.create(ip+":"+port,"kuaidaili"))



    def close(self,spider):
        proxy_pool.crawl_proxy_task(proxy_list)
        proxy_pool.check_ip_availability_task()





