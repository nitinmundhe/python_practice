from threading import Thread,Lock
def add(a,b):
    return a+b
def sub(a,b):
    return a+b

r1 = add(10,20)
r2 = sub(10,20)
print(r1)
print(r2)


class MyThread(Thread):
    def __init__(self,func,x,y):
        self.f = func
        self.arg1 = x
        self.arg2 = x
        self.status = None
        super().__init__()

    def run(self):
        print('Start of Thread ...')
        mylock.acquire()
        r = self.f(self.arg1,self.arg2)
        mylock.release()
        print(self.f.__name__)
        print('Result is ',r)
        self.status = 'Success'
        print(self.status)


mylock = Lock()

t1 = MyThread(add,20,10)
t2 = MyThread(sub,20,10)
t1.start()
t1.join
t2.start()

# Priority Queue

from queue import Queue
q = Queue(4)
t3 = MyThread(add,30,40)
t4 = MyThread(sub,40,50)

q.put(t3)
q.put(t4)

r1 = q.full()
r2 = q.empty()
r3 = q.qsize()

print(r1,r2,r3)

while q.empty() == False :
    print('Inside while')
    t = q.get()
    t.start()
    t.join()
    print('Outside while')