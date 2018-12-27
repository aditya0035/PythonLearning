import functools
User={"Username":"Aditya",'access_level':"guest"}

def User_secure_function(fn):
    @functools.wraps(fn)
    def secure_func(panel):
        if User.get("access_level")=="guest":
            return fn(panel)
    return secure_func

@User_secure_function
def myfunction(panel):
    return "XYZ"

print(myfunction("Admin"))

"""
The issue with this decorator is that we can't apply this decorator to any other function
"""

@User_secure_function()
def foo():
    return "FOO"

print(foo()) #error in either way if pass a value or not pass a value
