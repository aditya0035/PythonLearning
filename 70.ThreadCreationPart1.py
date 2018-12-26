def ask_user():
    user_input=input("Enter Your Name")
    greet=f'Hello{user_input}'
    print(greet)

def Complex_Calculation():
    print("Starting Calculation")
    x=[x**2 for x in range(10000000)]
    print("Ending Calculation")

"""
here if we run both program in sequential way under main thread
"""
ask_user()
Complex_Calculation()

