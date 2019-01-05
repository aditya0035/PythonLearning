var_list=[]
print(type(var_list))

var_tuple=()
print(type(var_tuple))

var_set=set()
print(type(var_set))

var_dict={}
print(type(var_dict))

var_list=["Jose","Jin","Rose","Jack"]
print(var_list)

var_tuple=("hello",)
print(var_tuple)
var_tuple="hi",
print(var_tuple)

var_tuple=("Hi","Hello","GoodMorning")
print(var_tuple)

var_set={"Hi","Hello","Good Morning"}
print(var_set)

var_dict={"key1":"hi","key2":"hello","key3":"Good Morning"}
print(var_dict)



'''Difference b/w tuple set and dict
1.set are unordered and mutable
2.list and dict are ordered and mutable
2.tuples are also ordered but immutable
'''

# as set does not have order so we can't acces them using indexing
# dict is extension of set and are accesiable using key

var_list.append("Jimmy") #this will append the element at the last of the list
#var_tuple.append() #not possible due to immutablity
#var_set.append() #not possible as no fixed order
#so add element in set use below
var_set.add("Good Night")

var_tuple=var_tuple+("one More",) #this will create a new tuple and assign that to it

var_set.add("Hi")
print(var_set) #not added as set does not allow duplicate so as dict as its a extension of set