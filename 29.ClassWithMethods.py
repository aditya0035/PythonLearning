"""
In python class method are defined just like function 
but it has an additional parameter which is first parameter 
self represent current instance as it has to acces the properties from that object
These method are called instance method as they work on instance/object of the class
example
"""
class Student:
    def __init__(self,name):
        self.Name=name
        self.Marks=[]
    def average(self):
        return sum(self.Marks)/len(self.Marks)

jignesh=Student("Jignesh")
jignesh.Marks.append(40)
jignesh.Marks.append(80)
jignesh.Marks.append(90)
jignesh.Marks.append(70)
jignesh.Marks.append(90)
print(jignesh.average()) #here it is equivelent to this
#the python will do like this
#ClassName.InstanceMethodName(Object,OtherArgs..)
print(Student.average(jignesh))
#although we can give anyname to self but its a standard convenstion in python to use self to refer object instance
#Self is the first parameter of an instance method of a class
#here we write self.Name so these are property of instance/self so these will varies from object to objects
#we can also put the object inside a like below

my_friend_list=["Aditya","Ramesh","Ashish"]
student_list=[Student(name) for name in my_friend_list]
print(student_list) #here it is the list of student object



        