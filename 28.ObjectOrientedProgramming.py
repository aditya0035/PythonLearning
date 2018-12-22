'''
object are those which store data and action 
class are the bluprint of object defined as 
class <className>(object):
    def __init__(self):
        <this method is used to initalize the variables>
        this method is responsiable for adding varibales and data to the object
    
'''
"""
single _ is used for private variable decleration
__init__ is the special function which is automatically invoked by python
while object creation and add all the property into that object using this method
self parameter represent the object(current)

"""
class Student(object):
    def __init__(self,name,school):
        self.Name=name
        self.School=school

"""
Object Creation in python
object are created by calling class name and pass the parametrs required by __init__(dunder init) method
"""
rajesh=Student("Rajesh","KNIT")
print(rajesh.Name)
print(rajesh.School)

"""
Here when we call Student() the python will create empty object then it will immediately call __init__ with supplied 
argument and assign them to the variables
so the self refer the current object which is created by python
and then python implicit call rajesh.__init__() function
"""
print(rajesh.__class__) # <class '__main__.Student'> here main is the module or __name__ and Student is the class

