# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy import Request
from msic.proxy.proxy_pool import proxy_pool
from msic.proxy.proxy import Proxy
from scrapy_splash import SplashRequest
from spiders.free_proxy_list_lua_source import *
from spiders.kuaidaili_lua_source import *
proxy_list = []

class IPPoolSpider(scrapy.Spider):
    name ="ip_pool"
    start_urls =[
        'http://www.kuaidaili.com/proxylist/%d/' %i  for i in range(1,10)
    ]
    start_urls =[
        'http://www.xicidaili.com/nn/',
        'https://free-proxy-list.net/',
    ]
    
    start_urls = ['http://www.xicidaili.com/nn/']

    def __init__(self,crawler):
        self.crawler = crawler
        dispatcher.connect(self.close,signals.spider_closed)

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def start_requests(self):
        for url in self.start_urls:
            if url.find("free-proxy-list")!=-1:
                yield SplashRequest(url, self.parse_free_proxy_list,endpoint = '/execute', method = 'GET',args={'wait': 0.5,'lua_source':free_proxy_list_lua_source()})
            elif url.find("us-proxy")!=-1:
                yield SplashRequest(url, self.parse_free_proxy_list,endpoint = '/execute', method = 'GET',args={'wait': 0.5,'lua_source':free_proxy_list_lua_source()})
            elif url.find("xicidaili") !=-1:
                proxy = "http://%s" % proxy_pool.random_choice_proxy(True)
                print(proxy)
                yield SplashRequest(url, self.parse_xicidaili,endpoint='/render.html',method='GET',args={'wait':0.5,'timeout':10,'proxy':proxy})
            elif url.find("kuaidaili")!=-1:
                yield SplashRequest(url, callback=self.parse_kuaidaili,endpoint='/execute',args={'wait':0.5,'lua_source':kuaidaili_lua_source()})


    def parse_free_proxy_list(self,response):
        str_list = response.text.split('\n')
        for str in str_list:
            if str.find("IP Address")==-1:
                ip_info = str.split('\t')
                if(len(ip_info)==5):
                    ip = ip_info[0]
                    port = ip_info[1]

                    proxy_list.append(Proxy.create(ip+":"+port,"free-proxy-list"))
                    
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
        #proxy_pool.check_ip_availability_task()





