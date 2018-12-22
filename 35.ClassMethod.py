"""
Class method are those method which are part of class
and called based on class basis
when we call class method from object it will pass that class to the class 
the first argument of the class method is the cls 
"""
'''
class Currency:
    def __init__(self,amount):
        self.amount=amount
    def addition(self,amount1,amount2)
        return Currency(amount1+amount2)
    
'''
"""
So here if user have to get the currency object from
sum of two number he has to first create instance and then call the method
which is unnessary
"""
'''
Euro=Currency(120)
amount=Euro.addition(1340,12923)
'''
"""
Here we can make this insatance method as static but if we have a class of Euro and we whant to get Euro Object then We have to 
Make this method as class method

"""
class Currency:
    def __init__(self,amount):
        self.amount=amount
    @classmethod
    def GetSum(cls,amount1,amount2):
        '''
        Here the compiler will automatically pass the class from object on which we call this method 
        '''
        return cls(amount1+amount2)
    def __repr__(self):
        return "<{0}>".format(self.__class__)

class Euro(Currency):
    def __init__(self,amount):
        super().__init__(amount)
    
    
c=Currency(10)
c.GetSum(10,14)
print(c)
        
e=Euro(10)
e.GetSum(10,15)
print(e)


"""
Note:Class method are used when we have to access to the class
Static method are used which are not depenedent on class and on instance
Although it a good practice to use class method over static method as class method are a good wrapper over static method
"""