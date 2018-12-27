"""
Function which can accept multiple arguments
"""

def add_all(a1,a2,a3,a4,a5):
    return a1+a2+a3+a4

print(add_all(1,2,3,4,5))

val=(1,2,3,4,5)

print(add_all(*val)) #argument unpacking

val={'a1':1,'a2':2,'a3':3,'a4':4,'a5':5}
print(add_all(**val)) #keyword arguments

def Add_all(*args): #so here *args will accept any no of positional arguments
    print(args) #(1, 2, 3, 4, 5,....) a tuples
    return sum(args)

Add_all(1,2,3,4,5)

def Add_Alls(**Kwargs): #so kwargs supports keywords argumenst
    print(Kwargs) #{'a': 1, 'b': 2, 'c': 3, 'd': 4} a dictionary

Add_Alls(a=1,b=2,c=3,d=4)


def Pretty_Print(*args,**kwargs):
    pass

"""
For this function we can pass any no of arguments
and note that args comes first the kwargs
args:We can accept any no of precisional argumenst
kwargs:We can accept any no of keyword arguments

Remember args comes befor then kwargs
by this help we can make a generic decorator
"""

"""
Function which can accept multiple arguments
"""

def add_all(a1,a2,a3,a4,a5):
    return a1+a2+a3+a4

print(add_all(1,2,3,4,5))

val=(1,2,3,4,5)

print(add_all(*val)) #argument unpacking

val={'a1':1,'a2':2,'a3':3,'a4':4,'a5':5}
print(add_all(**val)) #keyword arguments

def Add_all(*args): #so here *args will accept any no of positional arguments
    print(args) #(1, 2, 3, 4, 5,....) a tuples
    return sum(args)

Add_all(1,2,3,4,5)

def Add_Alls(**Kwargs): #so kwargs supports keywords argumenst
    print(Kwargs) #{'a': 1, 'b': 2, 'c': 3, 'd': 4} a dictionary

Add_Alls(a=1,b=2,c=3,d=4)


def Pretty_Print(*args,**kwargs):
    pass

"""
For this function we can pass any no of arguments
and note that args comes first the kwargs
args:We can accept any no of precisional argumenst
kwargs:We can accept any no of keyword arguments

Remember args comes befor then kwargs
by this help we can make a generic decorator
"""

