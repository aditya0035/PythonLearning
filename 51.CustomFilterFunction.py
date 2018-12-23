"""
as we know that filter function return a generator so we can create a custom generator as below
"""
def CustomFilterFunction(func,iterable):
    for i in iterable:
        if func(i):
            yield i
            
    