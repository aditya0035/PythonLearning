"""
These Keyword are new keyword
Get rid of yeild keyword
"""

from types import coroutine
from collections import deque
friends=deque(["Rolf","Joe","Chales","Kim","Stanley"])

@coroutine
def friend_upper():
    """
    This is a generator  which ccn some how receive data so we have to say python that this is
    a co-routine type
    """
    while friends:
        friend=friends.popleft().upper()
        greeting=yield
        print(f'{greeting} {friend}')

async def greet(g):
    """
    Tell python that we have and async function which can await for a co-routine
    :param g: co-routine
    :return:
    """
    await g
    """
    Here await is like yield from 
    awit tell python that wait for co-routine to finish 
    but we can suspend the function in middle
    if there is anything after awit it will not execute till the g finish its execution 
    """


async def Greet(g):
    print("Starting")
    await g
    print("Ending") # it will execute when the g finish its excution
    """
    Note:Suspending and Finish are two different terms
    """
f=friend_upper()
g=greet(f)
g.send(None)
g.send("Good Morning")