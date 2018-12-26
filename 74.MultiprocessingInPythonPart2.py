"""
like Threadpoolexecutor we have ProcessPoolExecutor in Concurrent.futures module
which will take care of all the process creation like thread pool executor does
"""
from concurrent.futures import ProcessPoolExecutor
def ask_user():
    user_input=input("Enter Your Name")
    greet=f'Hello{user_input}'
    print(greet)

def Complex_Calculation():
    print("Starting Calculation")
    x=[x**2 for x in range(10000000)]
    print("Ending Calculation")

def Complex_Calculation_without_Resource():
    x=[x**2 for x in range(10000000)]

if __name__=='__main__': #never forget that as in window when module load this file run
    with ProcessPoolExecutor(2) as pool:
        # pool.submit(ask_user)
        # pool.submit(Complex_Calculation)
        pool.submit(Complex_Calculation_without_Resource)
        pool.submit(Complex_Calculation_without_Resource)

#in this way we can get value from multiprocess
