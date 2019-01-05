'''In python we usually deal with exception using try except and finally block but apart
form this there is a one mor block which is else block let see
we can rereaise erro using raise keyword
'''
def division(a ,b):
    try:
       c= a/b
    except ValueError:
        '''Here it is the way by which we can catch single error'''
        print('Value Error')
    except (ZeroDivisionError,TypeError) as ex:
        '''Here it is the way we can catch multiple erro using single except block'''
        '''Here we are printing the error which is called swallowing error instead we can re raise the error'''
        '''to re raise error we can just write raise with out any exception'''
        '''Or we can catch the error using as a variable like as ex and then throw that variable using raise ex'''
        print('error')
    else:
        '''This block will execute if there is no return from try and there is no error try'''
        print("Put the code which need to execute if try does not throw any exception")
        return c
    finally:
        print("This block will always execute whatever there is error or not it does not execute is ex")


print(division(10,5))
division(10,0)


