"""
Like Threading we can create different process bt the issue with process is that we can't  share a resource b/w them
also when we create a process it will run separately under a different thread

To Create Multiprocessing we have to import Multiprocessing Module
"""
from multiprocessing import  Process
from datetime import datetime
def ask_user():
    user_input=input("Enter Your Name")
    greet=f'Hello{user_input}'
    print(greet)

def Complex_Calculation():
    print("Starting Calculation")
    x=[x**2 for x in range(10000000)]
    print("Ending Calculation")

print(__name__)
if __name__=='__main__':
    print(__name__)
    proces1 = Process(target=Complex_Calculation)
    proces1.start()
    ask_user()
    proces1.join()


"""
Here we will get error as we are tryong to access resource termial which is running in main thread
So from this we can say that process does not share the resource easily
"""

"""
From This we can conclude that for waiting use multiThreading and process when no resource sharing required and need to
run thing concurrently
"""