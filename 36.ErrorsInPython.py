iation"""
In python error may occurs there are various type of errors in python
So we ave to trace the stack trace to find out where the error occurs
1.Index Error
2.Key Error
3.Name Error
4.Attribute Error
5.Not Implementation Error(can be thrown by us)
6.Runtime Error
7.Syntex Error
8.Indentation Error
9.Tab Error
10.Type Error
11.Value Error
12.Import Error
13.Depriciation Error
"""

"""
For Raising Error in python we use raise keyword
We can raise any error from above error but it will be good practice if we can raise our own error with custom message
for Custom Error we can create a class which can inherit from above classes or can inherit from exception class
"""
class Garage:
    def __init__(self):
        pass
    def addcars(self,car):
        raise notimplementederror("This Method is not implemented yet")

class customtypeerror(TypeError):
    def __init__(self,msg):
        super().__init(msg)

def custom_function():
    raise customtypeerror("Custom Error")

class custom_exception(exception):
    def __init__(self,msg),statuscode:
        super().__init__(f'msg:{msg},status:{statuscode}')

def custom_expception_function():
    raise  custom_exception("Not Found",404)
    