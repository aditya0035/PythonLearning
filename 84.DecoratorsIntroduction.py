"""
Decorator are higher order function which return a function
higer order function are function which take function as argument and they must return a function
here the input function is another function
if a function take other function as input but does not return a function its not a decorator
"""
user={"UserName":"Aditya","acesslevel":"Admin"}
#user={"UserName":"guest","acesslevel":"Guest"}

def user_has_permission(f):
    if user.get("acesslevel")=="Admin":
        return f
    raise RuntimeError

def my_function():
    return "Password is 1234"

my_secure_function=user_has_permission(my_function)
print(my_secure_function())

