class Student:
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self.marks=[]
    def average(self):
        return sum(self.marks)/len(self.marks)
class WorkingStudents(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary=salary
    @property
    def WeeklySalary(self):
        '''To Create properties use @property Decorator then the method is accesiable as propery'''
        return  self.salary*8*5

Rolf=WorkingStudents("Jose","MIT",200)
Rolf.marks.append(87)
Rolf.marks.append(92)
Rolf.marks.append(70)
Rolf.marks.append(78)
Rolf.marks.append(85)
print(Rolf.marks)
print(Rolf.WeeklySalary)