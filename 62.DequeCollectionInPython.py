"""
Dequeue collection is part of collection module and we need to import that
it allow us to insert element from both end
using append,pop,appendleft and popleft method
"""

from collections import deque

my_queue=deque();
my_queue.append("Aditya") #insert element from right
my_queue.append("Ashihs")
my_queue.append("Rahul")
my_queue.appendleft("Ankur") #insert element from left
print(my_queue)
my_queue.pop() #remove element from right
print(my_queue)
my_queue.popleft()
print(my_queue) #it will remove element from left


"""
We can create a dequeue from a list also when we pass iterable it takes elements of that iterables
and convert them into dequeue element by appending them 
"""