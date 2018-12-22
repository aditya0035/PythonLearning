my_friends=["aditya saraswat","anuj","Ashish","Ankur"]
"""
str.capitalize method capitalize first letter of string
"""
my_frineds=[friend.capitalize() for friend in my_friends]
print(my_frineds)

my_frineds=[friend.title() for friend in my_friends]
print(my_frineds)

my_frineds=[friend.lower() for friend in my_friends]
print(my_frineds)

my_frineds=[friend.upper() for friend in my_friends]
print(my_frineds)

"""
The title method of string make the starting letter of a word in the string capital
"""
'''
To See the the method of a class we can use below function
it show the doc string
1.dir(str) it will show all the method in that class
2.help(str) it will show all method with there doc string
3.help(str.title) it will show the doc string of title method
'''
