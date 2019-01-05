'''in python data can be store in object and also object has actions'''
'''Classes are blueprint of object  and defined using class keyword'''
class Students:
    def __init__(self,name,grades):
        '''this method is used for adding property to the constructed object and called by python itslef
        when python create object is empty
        '''
        self.name=name
        self.grades=grades
    def average(self):
        print(sum(self.grades))
        return  sum(self.grades)

'''Object creation in python is simple just call the class'''
Mark=Students("Mark",[65,78,90,95,97])
print(Mark.average())

'''Here self refer the object itself you can provide any name the python interpreter makes a call like that'''
Students.average(Mark) #its the way python make a call
'''We can pass any number of argument to a method but self is the first argument'''
'''these method which hase self as first argument are called instance methdo'''


