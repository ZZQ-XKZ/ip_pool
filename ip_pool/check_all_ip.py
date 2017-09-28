import argparse
from msic.proxy.proxy_pool import ProxyPool,proxy_pool


parser = argparse.ArgumentParser(description='Process some integers.')


parser.add_argument('--begin')
parser.add_argument('--end')
parser.add_argument('--count',action="store_true")
args = parser.parse_args()

if args.count ==True:
    print(proxy_pool.get_ip_count())
    exit()

if args.begin != None and args.end != None:
    count = proxy_pool.get_ip_count()
    begin = min(max(0,int(args.begin)),int(args.end)-1,int(count)-2)
    end=min(max(1,int(args.end),begin+1),int(count)-1)
    proxy_pool.check_ip_availability_by_range(begin,end)

