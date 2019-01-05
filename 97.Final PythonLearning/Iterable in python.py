'''iterable are those which have __iter__ method in it and this method return an iterator'''
'''iterables are those which has iter method and the iter method return a function(self) on which next method ca
be called 

we can define iterable either using iter or len and get item method
'''
class custom_iterable:
    def __init__(self):
        self.counter=1
    def __next__(self):
        if self.counter<=100:
            current=self.counter
            self.counter+=1
            return current
        else:
            raise StopIteration
    def __iter__(self):
        #return custom_iterable()
        #return self.genrator()
        return  self
    def genrator(self):
        while self.counter<=100:
            yield self.counter
            self.counter+=1


for i in custom_iterable():
    print(i)
