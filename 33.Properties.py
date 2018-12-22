"""
Function/Method are the one which perform some action
but property are those which need exposed value to other object 
"""
"""
In python properties are created using @property decorator this will turn a methdo in a propety
"""
class Student:
    def __init__(self,school):
        self.school=school
    @property
    def Name(self):
        return self.name
    @Name.setter
    def Name(self,value):
        self.name=value
    @Name.deleter
    def Name(self):
        del self.name

jhony=Student("MIT")
jhony.Name="Aditya"
print(jhony.Name)

class Garage:
    def __init__(self):
        pass
    def SetBrand(self,value):
        self.brand=value
    def GetBrand(self):
        return self.brand
    Brand=property(GetBrand,SetBrand) #here we have getter,setter,deleter method

ford=Garage()
ford.Brand="Ford"
print(ford.Brand)