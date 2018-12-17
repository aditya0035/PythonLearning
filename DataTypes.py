'''
Python has following types of DataTypes
1.Int:Whole numbers without decimal point
2.Floating Number:With decimal point
3.String:Sequence of characters,for computer which does not have meaning
but for human being they have
4.None:Default type of variable
5.Object

In python everything is treated as object there is no concept of primitive type
Variables:are anything which can hold a reference to the object
Conventions to Create Variables
1.Can begin with letters and _
2.Can't have any special symbol apart from _
3.Can have number but can't start with that
4.Can't a reserved keyword
5.python is a weakly type language so no type decleration required
6.A variable in python point to a memory location block which hold the data
7.By default type of variable is None if we didn't initialize that
'''

a = 12  # integer variable
b = 234567890032222222212  # Integer variables
c = 30.90  # floating point
d = 212312321333312333333333.0  # floating point number
e = "Aditya"  # string type
f = 'f'       # string variables
g = 'Aditya'  # string
# we can use single quotes and double quotes for string literal assignment
h = '''Aditya is
      a good boy '''
i = """Ravi is also a
good
boy"""

# we can create a multiline string using triple single quotes or triple double
# quotes if these are not assign to a variable these are treated as comments

j = 'Aditya\'s lunch box'

''' \ act as escape character as we have to tell interpreter that
don't consider '  as string terminator'''

''' escape character can be used anywhere for any symbols
which has special meaning in python'''

k = "Aditya's pan"
# we can use single quotes inside "" and vice versa

'''
 We can use type() function to see the type of all function
 print function is used to show the output on console window
 print show the string output for that it call the __str__ function
 or __repr__ function/method of the object
 the implementation of these two function define what will be show on console
 if a object does not implement __str__ function the print wil call __repr__
 to show output apart form that __repr__ is used for various functionality
 so its a good practice to implement that function if we have
 choice to implement  either of them
 '''
print("a : {0}".format(type(a)))
print("b : {0}".format(type(b)))
print("c : {0}".format(type(c)))
print("d : {0}".format(type(d)))
print("e : {0}".format(type(e)))
print("f : {0}".format(type(f)))
print("g : {0}".format(type(g)))
print("h : {0}".format(type(h)))
print("i : {0}".format(type(i)))
print("j : {0}".format(type(j)))
print("k : {0}".format(type(k)))
print("j:{0}".format(j))
print("k:{0}".format(k))