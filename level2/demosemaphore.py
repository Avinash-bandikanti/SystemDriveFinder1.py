from threading import *
import time
s=Semaphore(2)
def wish(name):
    s.acquire()
    for i in range(3):
        print("good evening:",end='')
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish,args=('jose',))
t2=Thread(target=wish,args=('mart',))
t3=Thread(target=wish,args=('orange',))
t4=Thread(target=wish,args=('mango',))
t5=Thread(target=wish,args=('apple',))
t6=Thread(target=wish,args=('banana',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()