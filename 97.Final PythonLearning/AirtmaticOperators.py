a=2
b=3
c=2.0
d=3.0
e="4"
f="4"
# Addition/Substraction/Multiplication int+int=int
print(a+b)
# Addition/Substraction /Multiplication int+float=float
print(a+c)
# Addition/Substraction /Multiplication float+float=float
print(c+d)
# Addition string+int
# print(e+a) will give error
# Addition string+string=concatenation /Substraction Not possible for strigs
print(e+f)
# Multiplication of string
print(e*a)  # string*int repeat the strings that no of times
# (string*float) not possible error
# (string)*(string) not output error

# Divison Operator
# int/int =float 1.45 or 1.0
print(a/b)
# int/float=float
print(a/c)
# float/float=float
print(c/d)
# string/(number) not possible
# print(e/a)
# string/string not possible
# print(e/f)

#Integer Division Operator
#int//int=int
print(a//b)
#float//float =float
print(c//d)

# Modulous Operator --Provide reminder
print(a%b)  #int%int=int
print(c%d)  #float%float=float

#Follow BODMAS but if two operator has same precedence then follow left to right rule

#Exponential Operator work only on numbers
print(a**b)
print(c**d)

#Note: While using with range itrables here / gives float and range require both integer so  below will not work
'''for i in range(1, (12/6)):
    print(i)
'''

#use as range works the same way as string range work i.e first inclusive last exclusive
for i in range(1, (18//6)):
    print(i)


