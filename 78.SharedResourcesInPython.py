"""
We can use queue for managing shared resources
"""
import time
import random
from queue import Queue
from threading import  Thread

counter=0
counter_queue=Queue()  #conunter incresement
job_queue=Queue()  #things to be printed

def Counter_Manager():
    global counter
    while True:
        incresment=counter_queue.get() #this will wait until a new item avaliable then lock the queue and then it will not allow any thread to access this
        old_counter=counter
        counter=old_counter+incresment
        job_queue.put((f'New Counter Value is {counter}',)) #here what we put in the queue has to be tuple
        counter_queue.task_done() #this will release the lock and make it avaliable i.e. unlocks the queue and thread can access that

def Printer_Manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()

Thread(target=Counter_Manager,daemon=True).start() #Daemon Thread are the threads which are always running until it found an error
Thread(target=Printer_Manager,daemon=True).start() #Daemon Thread are Continuously running threads

def Incresment_Counter():
    counter_queue.put(1)

worker_threads=[ Thread(target=Incresment_Counter) for x in range(10)]

for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join()