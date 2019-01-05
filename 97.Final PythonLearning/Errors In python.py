#in python there are various kinds of error
'''We can have error while executing python as error occured at run time  we classifed error as below'''
'''
1.Index error: occur when index is out of range
2.Key Error:When trying to acces a element in dic which does not exists
3.Name error:when trying to use a variable which is not declared
4.Attribute error:when trying to call a method which is not exists in the module
5.Not implemented error:Used by us when we trying to call a method which is not implemented
6.Runtime Error:all error are runtime error
7.Syntext Error:occurs when we miss a syntex
8.Indentation error:as python is indented language so it @some place indent is missed
9.Tab error:if we are using tabbing for indentation and we missed tabing at some place
10.Type Error:when we trying do some incompatiable operation on different types
11.values error:occurs when we trying to parse same value but format is different like float to int
12.Import error when we trying to import some functionality from a module which cause circular dependency 
13.Depreceation warning:its warning not error so occurs when we are using certain module or update a module 
and some method are now modified and old methods are 
use raise keyword to raise a error
'''

def not_implemented_error():
    raise NotImplementedError("This Method is not implemented")

def type_error():
    raise TypeError("This is the type error")
#not_implemented_error()
type_error()
'''
instead of raising system defined error it will be good if we can raise our own error
As that will contains the code which we want and also serve our purpose
when can do this by extending any of the error classes
'''