'''
python has below operator
1.__add__ represented as +
2.__sub__ represented as _
3.__multi__ represented as *
4./ division operator
5.// Floor Division Operator
6.** exponatial/multiplier operator
7.+= __iadd__
8.-= __isub__
9.*=
10. /= 
these all oerator are called self assignement operator
11.= assignment operator
'''
a = 12
b = 23
c = 20.0
d = 23.2
f = "Aditya"
g = "Saraswat"
print("a+b:{0}".format(a + b))  # int+int=int,float+int=float
print("a-b:{0}".format(a - b))  # int-int=int,float-int=float
print("a*b:{0}".format(a * b))  # int*int=int,float*int=float
print("a/b:{0}".format(a / b))  # int/int=float,float/float=float
print("a//b:{0}".format(a // b))
# int//int=int(w/o remineder) float///int=float
print("a%b:{0}".format(a % b))  # int%int=int(remninder) float%float=float
print("c//d:{0}".format(c // d))
print("c%d:{0}".format(c % d))
print("a**b:{0}".format(a**b)) 
# this gives the power of a to the b works with int and float
'''we can't do the +,-,/,//,% operators on different type i.e.
 we can't add a number to a string first we have to make them 
 similar datatype'''
'''
 string does not support -,/,//,% operators
 + used to concatenate the string and each time a new string is returned as 
 strings are immutable
 * act as mutiplier that is it repeat the string that number of times
'''
'''
For Complex airthmatic operator please follow 
BODMAS rule
and when two operators having same precidence the 
follow left to right
Bracket,
Exponent
Division,Multiplie
Addition,Substraction
'''
print("f+g:{0}".format(f + g))
print("f**2:{0}".format(f ** 2))