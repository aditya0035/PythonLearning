"""
In this we will learn more about some more function
1.Any
2.All
3.Enumerate
Any will check if any of the value in the iterable is return true if true then will make true
All check if all the value in the iterable are true then if all the value becomes true then true
and if any value is false then it will retrun false
enumerate:it will take iterable as input and return index and value from iterable as ouput which then can be used
with other iterable
"""
list_num=[1,2,3,4,5]
print(any(list_num))
print(all(list_num))
list_num=['aditya',None]
print(any([]))
print(all([]))
print(all(list_num))
print(any(list_num))
list_num=[1,2,3,4,5]
for index,value in enumerate(list_num):
    print(f"index:{index},value:{value}")