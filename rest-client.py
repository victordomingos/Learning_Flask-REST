#! /usr/bin/env python3

import requests
import timeit
import threading
from time import sleep

start = timeit.default_timer()

def get_req():
    data = requests.get("http://127.0.0.1:5000")
    print(data.text)
    #sleep(1)


for i in range(1000):
    #get_req()
        
    print("--------->", i)
    daemon = threading.Thread(target=get_req)
    # daemon.setDaemon(True)
    daemon.start()

daemon.join()
end = timeit.default_timer()
print(end-start)

