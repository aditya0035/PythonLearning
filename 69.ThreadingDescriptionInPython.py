"""
Dining Philospher Problem
5 Philoshpher 5 spoon infinite hunger
2 spoon required to feed
1 waiter
2min time
Note:Nothing can happen concurrently even in python
"""

"""
Process:A thread with all the required resource needed to execute the block
once avail it become process
Thread:Thread a unit which represent a block of code which need to be executed
"""
'''
If a cpu has 4 core that mean it can run four threads and it means it can run 4process
simultaneously

The thread are the one which run on the core but prcess is a wrapper around thread
A thread waiting for its execution is called waiting thread as no resource is assigned to it
'''
"""
Prcess=At least one thread+Some Resources set aside by OS eg core network
These resources continously changes as the process need change.
Process Manage all the Resources which is needed by a thread
"""
"""
Waiting Thread          Running Thread  Core
T1                          t5          1
T2                          t6          2
T3                          T7          3
T4                          T8          4

Here T1,T2,T3,T4 are waiting thread waiting for there execution as they don't have any resources for there execution
t5,t6,t7,t8 are running thread which runs on core 1,2,3,4
And So these thread now have resources required for there execution
it might happen that t5,t6 may be part of same process
Process can work independently and can communicate with other process

One thread can run at one core at a time
If we have two cores and a process need two thread for execution then it can execute for a long time
As we have waiting thread in real world problem so we need time slicing which means that we will execute each thread
for a fixed amount of time and then we will execute the waiting thread so they will not starve
but this time slicing is not free it required resource to save the state of each running thread to somewhere 
so that when we pull them further for execution then we will not start from begaining.
"""

"""
About Python MultiThreading
Python Work on the principle of GIL(global Interpreter lock)
When we launch a module  we get a new python process that is we get at least one thread 
within python,we get one starting thread which start executing our code is called main thread
but we can make more

Due to GIL concept in python we can't run two threads in one process at the same time.
that is if we have main thread and other thread in python we can't execute both thread at the same time even we have
multiple processor its because Each Process in python creates a key resource when a thread is running,it must acquire
that resource and every process create a unique key resource.due to one key resource only one thread can run in a process
at a time

This key Resource is called GIL(global interpreter lock)

So we can create different python module and each module will have different key resource
and have their own thread but here the issue is that they become two different process so the sharing of data 
will not be easy

So now the question arises is whats point of threading in python
"""
"""
So in python threading is useful for these kinds of scenarios 
1. we have a program in which we have to take input from user 
and apart from that we have a function who will perform a long running calculation which is independent to user 

So in this scenario we have to wait to that time till the user provide input and then will be able to perform second task

if we perform that app in single thread then if we call 1 then 2 operation or 2 operation then 1 then still it will
take reasonable amount of time

Although we can reduce this time using Co-operative multiple tasking like
1.Ask user for input and then immediately release the GIL and now Our Complex Calculation thread will acquire the GIL
and start doing calculation and once user provided input release the lock will be acquire by main thread and
will show the o/p to console and then release GIL which will be acquire by complex operation thread and complete that
So in python we can reduce the waiting time when one thread is doing a  blocking operation

As OS give priority to that thread which is doing things so if a thread is waiting it will run less frequently
"""