"""
In python we can create function without arguments.
below is the syntex of function w/o arguments
def <functionName>():
    <function body>

if no return type is specified that mean the function will return None as default
we can return anything from function that is it can return a number,string,datastructure,
another function,a class instance etc
"""
def greet():
    print("Welcome to python!")

#after function creation we need to call it also function should be declare first before using it

#below is tha way to call a function
greet()

#if a function is going to return something then we call them as below
result=greet()
print(result)
