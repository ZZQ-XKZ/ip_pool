from msic.common import utils
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,Boolean,Float
import re
Base=declarative_base()

def check_ip_validity(ip):
    aa=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$",ip)
    if aa:
        return True
    else:
        return false
class Proxy(Base):
    __tablename__='proxy'
    ip = Column(String(25),primary_key=True)
    origin=Column(String(256))
    create_time=Column(DateTime)
    update_time=Column(DateTime)
    last_use_time=Column(DateTime)
    failed_count=Column(Integer)
    used_count=Column(Integer)
    internal_response_speed=Column(Integer)
    external_response_speed=Column(Integer)
    internal_weight=Column(Float)
    external_weight=Column(Float)
    internal_validity=Column(Boolean)
    external_validity=Column(Boolean)
    
    @staticmethod
    def create(ip, origin):
        if check_ip_validity(ip) == False:
            return None
        proxy = Proxy()
        proxy.ip = ip
        proxy.origin = origin
        proxy.create_time = utils.get_utc_date()
        proxy.update_time = utils.get_utc_date()
        proxy.last_use_time = utils.get_utc_date()
        proxy.failed_count = 0
        proxy.used_count = 0
        proxy.internal_weight = 0.0
        proxy.external_weight = 0.0
        proxy.internal_response_speed = -1
        proxy.external_response_speed = -1
        proxy.internal_validity = True
        proxy.external_validity = True
        return proxy
        



    @staticmethod
    def create_table(engine):
        Base.metadata.create_all(engine)
