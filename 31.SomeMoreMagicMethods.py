"""
__repr__(self)
this method is used to print out string representation of object
"""
class Garage:
    def __init__(self):
        self.cars=[]
    def __repr__(self):
        return '<Garage has {0} cars>'.format(len(self.cars))
    

ford=Garage()
ford.cars.append("Fiesta")
ford.cars.append("Focus")
print(ford)

"""
Similarly we have __str__ function which return string whose solely purpose is to provide some imfomation to the end user about the object
str() is used for creating output for end user while
 repr() is mainly used for debugging and development.
 repr’s goal is to be unambiguous and str’s is to be readable.
"""
class garage(object):
    def __init__(self):
        self.cars=[]
    def __str__(self):
        return "<This object is responsiable for Garage Creation>"

ford=garage()
print(ford)
print(garage.__str__(ford))

"""
These all methods are defined in object class by default every class inherit from object class
Apart from there are some other magic methods
1.__add__ responsiable for addition of two object can return a new object or modify the object
2.__iadd__ responsiable for addition like += can return same object or new object
These above methods are refer as operator overloading
"""

"""
Note:If we have to implement one of from __repr__ or __str__ try to implement __repr__ 
"""