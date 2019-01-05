'''Queue are collection which work on principle of FIFO
In queue element are inserted from one end and remove from other end
A queue in which element can can inseretd and removed from both end is doubly eneded queue of dequeue
[1,2,3,4,5,6]
Here append which append element at right end
pop will remove element from left
appendleft will insert element from left and pop will remove element from right
'''

'''Stack are collection in which element follow LIFO liek a stack of coin
'''
class queue:
    def  __init__(self):
        self.elements=[]
    def append(self,element):
        self.elements.append(element)
    def pop(self):
        self.elements.pop(0)
    def __len__(self):
       return len(self.elements)
    def __getitem__(self, item):
        return self.elements[item]

Queue=queue()
Queue.append("123")
Queue.append("345")
Queue.append("123")
Queue.pop()
for element in Queue:
    print(element)