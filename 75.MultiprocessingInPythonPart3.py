from multiprocessing import Process,Manager
def ask_user():
    user_input=input("Enter Your Name")
    greet=f'Hello{user_input}'
    print(greet)

def Complex_Calculation():
    print("Starting Calculation")
    x=[x**2 for x in range(10000000)]
    print("Ending Calculation")
    return x

if __name__=="__main__":
    result = {}
    result = Manager().dict()
    process1 = Process(target=Complex_Calculation)
    process2 = Process(target=ask_user)
    x = process1.start()
    y = process2.start()
    process1.join()
    process2.join()
    print(x)
    print(y)
    print(result)