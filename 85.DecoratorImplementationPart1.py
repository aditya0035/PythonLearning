"""
In part1 that was a very simpler way of decorator
but we do it in different way Normally we define the decorator differently
"""
user={"UserName":"Aditya","acesslevel":"Admin"}
def User_has_permission(f):
    def Secure_function():
        if user.get("acesslevel")=="Admin":
            return f()
    return Secure_function

def my_function():
    return "Password is 1234"
"""
Here the secure_function will check the condition and will actually run the function 
and we will be going to return secure function
"""
my_secure_function=User_has_permission(my_function)
print(my_secure_function())

"""
it was the normal way of creating and returning decorator
"""