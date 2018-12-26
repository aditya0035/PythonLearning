"""
Atomic Operation:That can't be interrupted at middle
e.g. print before we remove the thread from queue
"""

from threading import Thread
import  time
import  random
counter=0
def Incresment_Conuter():
    global counter
    time.sleep(random.randint(1, 10))
    counter+=1
    time.sleep(random.randint(1, 10))
    print(f'Now Counter Value is {counter}')
    print("------------------")
threadList=[]
for x in range(10):
    t=Thread(target=Incresment_Conuter)
    time.sleep(random.randint(1, 10))
    t.start()
    threadList.append(t)
    print("Thread Started")
    """
    Here each time a new thread will be started
    """
for thread in threadList:
    thread.join()
"""
Here the thing are happening so fast that it looks  like the method is calling sequencely 
So see the actual behaviour we need to add some delay using time.sleep() this is called fuzzing in multithreading
as it help us to see the problem 
"""