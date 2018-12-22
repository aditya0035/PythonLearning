"""
In python we doesnot always need to create a list using 
for loop like
"""

my_list=[]
for i in range(10):
    my_list.append(i)

print(my_list)

'''
Using list comprehesnion we can create a list with a shorty hand syntex
'''

my_list=[i for i in range(10)] # this is known as list comprehension
print(my_list)

"""
List Comprehension with condition
"""
my_list=[]
for i in range(10):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)

"""
Using list comprehension
"""
my_list=[i for i in range(10) if i%2==0]
print(my_list)
my_list=[i**2 for i in range(10) if i%2==0]
print(my_list)
