import functools
User={"Username":"Aditya",'access_level':"guest"}

def Role_Decorator(Role):
    def User_secure_function(fn):
        @functools.wraps(fn)
        def secure_func():
            if User.get("access_level")=="guest":
                return fn(Role)
        return secure_func
    return User_secure_function

@Role_Decorator("Admin")
def myfunction(panel):
    return f'S {panel}'

@Role_Decorator(None)
def Foo():
    print("From Foo")
print(myfunction())


"""
So here is still a problem as our Decorator is not generic but we have one more wrapper around that
"""