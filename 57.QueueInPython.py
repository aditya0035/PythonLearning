"""
Queue in python are the based on the principle of first in and last out
so in queue from one end value get inserted and from other end value are removed
operation used are
1.pop
2.Append

Dequeue: Dequeue is the double ended queue that is in which from one end value are get inserted
and from other end value are removed but this work from both end
operation that works
1.append(add element from left end)
2.pop(remove element from left end)
3.appendleft
4.popleft
"""

class Queue:
    def __init__(self):
        self.queue=[]
    def append(self,value):
        self.queue.append(value)
    def pop(self):
        if len(self.queue)==0:
            pass
        else:
            self.queue.pop(0)
    def __len__(self):
        return len(self.queue)
    def __getitem__(self, item):
        return self.queue[item]


my_queue=Queue()
my_queue.append("Aditya")
my_queue.append("Saraswat")
for item in my_queue:
    print(item)
my_queue.pop()
my_queue.pop()
for item in my_queue:
    print(item)