"""
As in previous example we have created thread from Threading Module
Now we can create the Thread using Concurrent.Future Module
"""
from concurrent.futures import ThreadPoolExecutor
def ask_user():
    user_input=input("Enter Your Name\n")
    greet=f'Hello{user_input}'
    print(greet)

def Complex_Calculation():
    print("Starting Calculation")
    x=[x**2 for x in range(10000000)]
    print("Ending Calculation")

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(ask_user())
    pool.submit(Complex_Calculation())

"""
Here The Thread Pool Executor Will Create a pool of worker Thread with no target and allow us to use that pool to
execute our code as it worked in context manager so it will wait for pool to finish so we don't need to explicitly close
the pool
pool.shutdown()
"""

"""
Killing Of Thread:
We can write a code that can kill a thread but never kill a thread as it might happen that the thread is running some
code so it has GIL and we kill the thread in that case as the thread is kill so it will not able to release the GIL 
so our GIL will also gone so the thread which are waiting for GIL will starve to death so this situation cause deadlock
and tere is no solution to avoid this
"""