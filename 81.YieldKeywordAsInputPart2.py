from collections import deque
from typing import Generator
friends=deque(["Rolf","Joe","Chales","Kim","Stanley"])

def friend_upper():
    friend=friends.popleft().upper()
    greeting=yield
    print(f'{greeting }{friend}')

def greet(g:Generator): #this will prime the generator s
    g.send(None)
    while True:
        greeting=yield
        g.send(greeting)

f=friend_upper()
greeter=greet(f)
greeter.send(None)
greeter.send("Good Evening ")

"""
These kind of generators which has yield as input parameter is called Co-routine not generator in python
"""

