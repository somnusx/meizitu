from multiprocessing import Process,Queue
from chack import chack_run
from crawl import crawl_run

if __name__=="__main__":
    q = Queue()
    p1 = Process(target=chack_run,args=(q,))
    p2 = Process(target=crawl_run,args=(q,))
    p1.start()
    p2.start()