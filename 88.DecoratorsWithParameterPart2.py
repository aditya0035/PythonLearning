"""
So this is not a good approch so we need to make our decorators more generics
so we need to make a decorator that can take a parameters
"""
import functools
User={"Username":"Aditya",'access_level':"guest"}

def User_secure_function(fn):
    @functools.wraps(fn)
    def secure_func(panel):
        if User.get("access_level")=="guest":
            return fn(panel)
    return secure_func

@User_secure_function("Admin")
def My_Custom_func(panel):
    print(f'{panel}')

print(User_secure_function(My_Custom_func)("Admin")) #so here are we calling like this

