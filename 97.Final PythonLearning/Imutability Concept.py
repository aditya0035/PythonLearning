'''
in python the numbers(float,int,string) are immutable type i.e. when we do any opertion
the value assigned is new object
We can check memory location of a variable using id function
tuple are also immutable
+ always return new instance of the object i.e. amkes the object immutabke
+= make/modify the object
although it depend on the implementation of __add__(+) or __iadd__(+=)
for int float string,tuple both method return new instances
for list dict the + add new instance of these object but += modify the existing objects
e.g.
in python everything is object
'''
my_int=3
print(id(my_int))
my_int=5 #it will create a new object 5 and point the my_int to that location
print(id(my_int))

my_float=5.0
print(id(my_float))
my_float=10.0
print(id(my_float))

my_list=[10,15,90,55]
print(id(my_list))
print(id(my_list[0]))
my_list[0]=15
print(id(my_list))
print(id(my_list[0]))

print('----------tuple------')
my_tupel=([12,34,56,79],[12,35,67])
print(id(my_tupel))
print(id(my_tupel[0]))
print(id(my_tupel[0][0]))
my_tupel[0][0]=34
print(id(my_tupel[0][0]))
print(id(my_tupel[0]))
print(id(my_tupel))
print('-----Difference b/w + and +=-------------')
my_int=10
print(f'value:{my_int}:{id(my_int)}')
my_int+=15
print(f'value:{my_int}:{id(my_int)}')
my_int=my_int+10
print(f'value:{my_int}:{id(my_int)}')

string="aditya"
print(f'value:{string}:{id(string)}')
string=string+" Saraswat"
print(f'value:{string}:{id(string)}')
string+=" Good"
print(f'value:{string}:{id(string)}')

tuples=(12,14,15)
print(f'value:{tuples}:{id(tuples)}')
tuples=tuples+(13,16,17)
print(f'value:{tuples}:{id(tuples)}')
#tuples+=tuples(21,18)  no valid operation
#print(f'value:{tuples}:{id(tuples)}')

list=[23,24,25]
print(f'value:{list}:{id(list)}')
list=list+[26,27] #different address
print(f'value:{list}:{id(list)}')
list+=[28,29] #same address
print(f'value:{list}:{id(list)}')





