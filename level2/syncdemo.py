from threading import *
import time
def wish(name):
    for i in range(3):
        print("good evening:",end='')
        time.sleep(2)
        print(name)
t1=Thread(target=wish,args={'jose'})
t2=Thread(target=wish,args={'mart'})
t1.start()
t1.join()
t2.start()