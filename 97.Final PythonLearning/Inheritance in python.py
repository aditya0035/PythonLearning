class Students:
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self.marks=[]
    def average(self):
        return sum(self.marks)/len(self.marks)


#to avoid repeating code we can do inheritance to do inheritance we have to call super() to refer parent object
class WorkingStudent(Students):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary=salary

    def getSalery(self):
        self.salary*8.5*5


Rolf=WorkingStudent("Joe","MIT",200)
Rolf.marks.append(92)
Rolf.marks.append(65)
Rolf.marks.append(98)
Rolf.marks.append(83)
Rolf.marks.append(90)
print(Rolf.name)
print(Rolf.school)
print(Rolf.salary)
print(Rolf.average())

'''by super inheritance add extra properties to child object and inheritance is applicable from top to bottom'''
