"""
Inheritance:Means aquiring the property of parents and ablity to override them if needed
Inheritance also reduces the code repetation
In python inheritance is achieved like this
in inheritance the child object inherit parent property as well as methods

class <Child className>(<Inherited Parent Class Name>):
    def __init__(self):
        super().__init__(<pass the argument needed by parent>) this will create parent object

although we can omit the super call if no value needed by parent class __init__ method
"""
class Student:
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self.marks=[]
    def average(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary=salary
    def monthly_pay(self):
        return self.salary*5*30

James=WorkingStudent("James","MIT",3)
James.marks.append(78)
James.marks.append(89)
James.marks.append(90)
James.marks.append(97)
James.marks.append(87)
print(James.name)
print(James.school)
print(James.average())
print(James.monthly_pay())

#so by inheritance it will add extra parent property to the child object 
#Inheritance apply from top to bottom