"""
immutable mean we can't change the value each time we assign a new value new memory is allocated
for primitve type + (__add__) assign a new value and new memory allocation will be created
we can check that using id() method
as every thing in python is object that means strinn,int,float,bool,tuple are immutable
while list,dict,set are mutable that is when we do some manupulation a new object is not created
existing object is modified but these differ if we use + then a new object will be created and
if we use +=(__iadd__) then it will do modification over the same object
when we pass aargument to a function both point to same object but if we do some modfication over the
value then it will create a new value and point method local variable to that location
"""