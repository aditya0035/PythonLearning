'''in python function are defined using def keyword'''

def greeting():
    print("Good Morning")

greeting()

def function_with_args(name):
    print(f"Hello Mr.{name}")

function_with_args("Aditya")

def function_with_multi_args(args1,args2,args3):
    pass
function_with_multi_args(1,2,3)

'''Recursion:when a function call it self'''

'''by default function return none if no value or data structure is returned, we can return a a value from a function
 using return statement
 '''
def function_with_retun_value(args1,args2):
    return  args1+args2

print(function_with_retun_value(1,1))

print(function_with_multi_args(args1=1,args2=2,args3=3))

'''Varibale declared inside function does not have any outside scope'''

