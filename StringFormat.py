'''
in python we can format the string there are three ways in which one is 
supported in python version>3
1."string {0} Mr. {1}".format(args0,args1) here args can be variables
2."Sting {greet} Mr.{name}".format(greet=ags0,name=args1) here args0
and args1 can be variable or hardcoded value
3.f'{greet} Mr.{Name}' it is suported in python 3 rest above two are
supported in python 2.
here greet and name are variable name that we declared
'''
name = "Aditya Saraswat"
age = 25

print("{0} age is {1}".format(name, age))
print("{name} age is {age}".format(name=name, age=age))
# print(f'{name} age is {age}') supported in python version >3

'''Try to use f'{name} age is {age}' format method as it quite easy 
and readable '''