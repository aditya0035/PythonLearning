"""
Iterators are those which will implement __next__ method then any object can call next on them
"""
class FirstHundreadNumber:
    def __init__(self):
        self.number=0
    def __next__(self):
        if self.number<=100:
            current=self.number
            self.number=self.number+1
            return  current
        else:
            """
            These will raise stop iteration to stop the iteration once completed
            """
            raise  StopIteration() #it tell the python that we have reach the end of generator

instance=FirstHundreadNumber()
print(next(instance))
print(next(instance))
print(next(instance))

"""
These class will behave like generator but are iterator and call be called only via next method
Not all the iterators are generators
"""
#lst=list(instance)  #does not work as not iterable 
#print(list)

"""
in python 2 we create iterators using next method implementation
"""
"""
Also we can't call for each on iterators
"""
