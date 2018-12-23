"""
Iterables are those which implement __iter__method
and iterable return an iterators using __iter__ method
in  python there are two ways to genretae iterables
1.using __iter__ method implementation
2.or we can implement using __len__ & __getItem__
"""
"""
Iterator:Used to get the next value
Iterable:Used to go over all the value of iterator
"""

my_number=[x for x in [1,2,3,4,5]]
print(my_number) #here its list comprehension

"""
Similarly we can generate generator comprehension
"""
my_number_gen=(x for x in [1,2,3,4,5])
print(type(my_number_gen)) #<class 'generator'> it will create a generator
print(next(my_number_gen))
print(next(my_number_gen))

"""
Iterable creation
"""
class FirstHundreadNumber:
    def __init__(self):
        self.number=0
    def __next__(self):
        """Iterator block"""
        if self.number<=100:
            current=self.number
            self.number+=1
            return current
        else:
            raise StopIteration()
    def __iter__(self):
        return self

iterables=FirstHundreadNumber()
for numb in FirstHundreadNumber():
    print(numb)