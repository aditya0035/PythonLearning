"""
Named tuple are the part of collection module of python
Named tuple can store the item using name and can be accessed using that
Named tuple are like tuple but each element of the tuple has a name
"""

from collections import namedtuple

student=namedtuple("student",("name","school","age"))
#here above we define our named tuple schema that is name of the named tuple which should
#be same as variable name that is student and all the field which is part of that tuple
#so the field are name,school,age

my_tuple=student("Aditya","MIT",20) #now we are createing tuple based on that schema

print(my_tuple.name) #accessing element using that schema i.e. using name
print(my_tuple.school)
print(my_tuple.age)

"""
also we can convert existing tuple to named tuple as
"""
xyz_tuple=("Saraswat","California",23)
xyz_tuple=student._make(xyz_tuple)
print(xyz_tuple.name)

"""
Tuple Destructing
"""

name,school,age=xyz_tuple
print(name)

def function(name,school,age):
    print(f"name:{name},age:{age},school:{school}")

function(name=xyz_tuple.name,school=xyz_tuple.school,age=xyz_tuple.age)

