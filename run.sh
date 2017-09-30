#!/bin/bash
echo $1
command=$1
param=$2
if [ "$command" = "crawl" ]; then
    while true
    do
	scrapy crawl ip_pool
	python /app/ip_pool/check_all_ip.py --new
	sleep 30m
    done
fi;

if [ "$command" = "check" ]; then
    python /app/ip_pool/check_all_ip.py --new
fi;
