"""
In the python error handling is done using 
try,except,else,finally etc
the code which can throw exception is put inside try block
the except block is used for handling exception gracefully or for logging
else block is used to put code which can't throw exception and execute if try does not throw excption
finally block is always executed if exception happend or not 
it is used to handle the resource gracefully in case error ocuured
"""
def error_method(a,b):
    try:
        print("in try block")
        return a/b
    except TypeError as ex:
        print(ex)
    finally:
        #close the resource or file in this 
        # as it will always executed no matter what

"""
after except there we can place else block but when there is not return in try if try has a return then that will be a 
not reachable code. and also if no exception occurs in try then the else block will execute if exception happened
then it will not executed
"""
def divide_by_zero():
    try:
        print("in try block")
        #some error prone code goes here
    except TypeError as ex:
        print(ex)
    else:
        return a/b
    finally:
        #close the resource or file in this 
        # as it will always executed no matter what

"""
If required we can log the error and can reraise it using
raise keyword in except block it does not need object of error we can directly put like 
except TypeError as ex:
    log.info(ex)
    raise

here after raise no need to put ex
but if we are raising exception from other code of block apart from except then we need to pass the object in that case
"""
