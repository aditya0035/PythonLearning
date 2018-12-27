"""
Here we will see how to create and use decorator using @syntex
"""
import functools
user={"UserName":"Aditya","acesslevel":"Admin"}
def User_has_permission(f):
    @functools.wraps(f) #here it will keep the metadata of f
    def Secure_function():
        if user.get("acesslevel")=="Admin":
            return f()
    return Secure_function

@User_has_permission
# as here we already defined using decorator this is equivalent to user_has_permission(my_function)
def my_function():
    return "Password is 1234"

#so here we will call directly like
print(my_function())
print(my_function.__name__) #Secure_function
@User_has_permission
def foo():
    return "From FOO"

print(foo())
print(foo.__name__) #Secure_function

"""
So here its showing the wrapper name which is wrong we need to keep the metadata(like doc string,name) of original function
witf wrapper for that we need to use functools

functools  waraps around the decorator inner function so that it will keep the metadata of the function on which decorator
apply its simple this tell python that secure_function is a wrapper around other function

import functools
"""

"""
its always a good practice to use functools 
"""
"""
Here we will see how to create and use decorator using @syntex
"""
import functools
user={"UserName":"Aditya","acesslevel":"Admin"}
def User_has_permission(f):
    @functools.wraps(f) #here it will keep the metadata of f
    def Secure_function():
        if user.get("acesslevel")=="Admin":
            return f()
    return Secure_function

@User_has_permission
# as here we already defined using decorator this is equivalent to user_has_permission(my_function)
def my_function():
    return "Password is 1234"

#so here we will call directly like
print(my_function())
print(my_function.__name__) #Secure_function
@User_has_permission
def foo():
    return "From FOO"

print(foo())
print(foo.__name__) #Secure_function

"""
So here its showing the wrapper name which is wrong we need to keep the metadata(like doc string,name) of original function
witf wrapper for that we need to use functools

functools  waraps around the decorator inner function so that it will keep the metadata of the function on which decorator
apply its simple this tell python that secure_function is a wrapper around other function

import functools
"""

"""
its always a good practice to use functools 
"""
