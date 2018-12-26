"""
Yield Avoid Blocking Operation
Switching from one function(Suspended) to another function is cheaper then
Switching b/w thread
"""
"""
yielding from another iterator 
"""

from collections import deque
friends=deque(["Rolf","Joe","Chales","Kim","Stanley"])

def get_friedns():
    yield from friends

def greet(g):
    while True:
        try:
            friend=next(g)
            yield f'Hello {friend}'
        except StopIteration:
            pass

friends_generator=get_friedns()
g=greet(friends_generator)

print(next(g))
print(next(g))

"""
Here we are giving Data but by yield we can receive data 
"""

def greet():
    friend=yield  #here first call will suspend the function and then when we call next time with value that will be assign to friend
    print(f'Hello {friend}')

g=greet() #this is called generator intialization

"""
Yield in python is designed that it can suspend the function but then also we can recieve a value
after we resume it and the value we are recieveing will be going to that field
"""
g.send(None) #this is called priming of generator as it will run the function right up before to yield and will suspend the function
g.send("AdityaS")
"""
Here in this we are getting as exception as its a generator and when generator ends after we print there is 
no more repetition as nothing as to yield  so it will raise stop iteration 
"""
