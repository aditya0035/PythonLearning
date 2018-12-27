import functools
User={"Username":"Aditya",'access_level':"guest"}
def User_has_permission(func):
    @functools.wraps(func)
    def Secure_func(*args,**kwargs):
        if User.get("access_level") == "guest":
            return func(*args,**kwargs)
    return Secure_func


@User_has_permission
def my_function(Panel):
    print(f'{Panel}')

@User_has_permission
def another():
    print("another function")

print(my_function("Admin"))
print(another())
