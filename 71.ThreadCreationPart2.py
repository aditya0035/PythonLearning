"""
To Create thread in python we need to import Threading module
Here we are going to deal previous problem using thread
"""
from threading import Thread
def ask_user():
    user_input=input("Enter Your Name\n")
    greet=f'Hello{user_input}'
    print(greet)

def Complex_Calculation():
    print("Starting Calculation")
    x=[x**2 for x in range(10000000)]
    print("Ending Calculation")

Thread1=Thread(target=ask_user) #here it will going to OS and ask for a thread
Thread2=Thread(target=Complex_Calculation)
Thread1.start() #here it will start the thread
Thread2.start() #here it will start the thread
Thread1.join()# will make main thread to wait till the thread completed its execution
Thread2.join()# will make main thread to wait till the thread completed its execution

"""
So from this example we can say that thread are used for reducing waiting time if we are writing something which will
require CPU time all the time then there is no meaning of Creating Thread
"""




