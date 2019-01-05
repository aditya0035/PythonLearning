'''
This is the doc string which will give info about what this module will do
'''
class MyClass:
    '''
    This is the doc string which will give info about the class what it will do
    '''
    def  __init__(self):
        pass
    def my_method(self):
        '''
        this is the doc string which will explain what this method for
        what type of argument it will take
        what it will return
        :return:
        '''
        pass

'''We can see the doc string as'''
print(MyClass.__doc__)
print(MyClass.my_method.__doc__)
