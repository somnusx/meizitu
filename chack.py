import requests
import gevent
import re
from crawl import ua
from gevent import monkey
monkey.patch_all()


def chack(proxy,q):
    try:
        ip = proxy.split(':')[0]
        port = proxy.split(':')[1]
        proxies = {"http": "http://%s:%s" % (ip, port),
                   "https": "https://%s:%s" % (ip, port)}
        headers = ua()
        r = requests.get('http://jandan.net/', headers=headers, proxies=proxies, timeout=5)
        if r.ok:
            q.put(proxies)
            print q.qsize()
    except Exception, e:
        pass


def chack_run(q):
    url = 'http://www.66ip.cn/nmtq.php?getnum=10000&anonymoustype=3&proxytype=2&api=66ip'
    r = requests.get(url).text
    reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]):\d{2,5}')
    tasks = reip.findall(r)
    spawns = []
    for task in tasks:
        spawns.append(gevent.spawn(chack,task,q))
    gevent.joinall(spawns)

