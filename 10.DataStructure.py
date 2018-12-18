'''
In python below are the datastructures
1.List
2.Set
3.Tuple
4.Dictionary
'''

friend_list = []  # this will create empty list
friend_list = ["Jose", "James", "Jack", "Jim"]
print(friend_list)
friend_tuple = ('Jose', 'Jame', 'Jack', 'Jim')
print(friend_tuple)
single_friend_tuple = ('Aditya')
print(single_friend_tuple)  # its not a tuple to make tuple add , at end
single_friend_tuple = ('Aditya',)
print(single_friend_tuple)
friend_set = set()
print(friend_set)
friend_set = {'Jose', "James", "Jim", "Kim"}
print(friend_set)
friend_dic = dict()
print(friend_dic)
friend_dic = {'Jose': 10, 'James': 15, 'Kim': 0}
print(friend_dic)
'''
Note Keypoint about DataStructure
1.List and tuple mantain the order of the element
2.Set,dic(Now it hold) does not maintain the order they lost the order in which element are inserted
3.tuples are immutable i.e. once it is defined we cant add element if we add using + it will give new tuple
4.+ __add__ operator return new instance of these list,tuple,Dic,Set while
5.+= __iadd__ operator perform operation over the same object for list,dic,set
6.List,tuple element can be accessed using zero based index as they maintain their order
7.Set and Dic are not accesseable using Index dictionary is accessiable using key
8.As List maintain order we can use .append method to inset element and it will goes to last
9.for dictionary we use the syntex dict[key]=value it will insert the key along with value
10.Set does not contains any duplicate record
11.Dictionary is extension of Set and its key Should be unique i.e it does not allow duplicate key while value can be duplicate
12.for inserting element in set use add method 
13.you can use the id method to check for object reference
'''
print(friend_list[1])
print(friend_tuple[0])
# print(friend_set[0]) does not support indexing
#print(friend_dic[0]) KeyError: 0 as dic always search using key
print(friend_dic["James"]) #key is case sensitive in python
friend_list.append("Ramesh")
print(friend_list)
#friend_tuple.append("Ramesh") # AttributeError: 'tuple' object has no attribute 'append'
print(friend_set)
friend_set.add("Ramesh")
print(friend_set)
friend_set.add("Ramesh")
print(friend_set)
print(friend_dic)
friend_dic["Ramesh"]=30
print(friend_dic)
print("---List Address Concept----")
print(friend_list)
print(id(friend_list))
friend_list=friend_list+["Hero Alam"]
print(id(friend_list))
print(friend_list)
friend_list+=["Alam"]
print(id(friend_list))
print(friend_list)

print("---tuple Address Concept----")
print(friend_tuple)
print(id(friend_tuple))
friend_tuple=friend_tuple+('Alam',)
print(id(friend_tuple))
print(friend_tuple)
friend_tuple+=('Hero Alam',) #new address as immutable
print(id(friend_tuple))
print(friend_tuple)

print("----Set Address Concept---")
print(friend_set)
print(id(friend_set))
#friend_set=friend_set+{'Alam'} Set does not support these
print(id(friend_set))
print(friend_set)
#friend_set+=('Hero Alam',) #new address as immutable
print(id(friend_set))
print(friend_set)

