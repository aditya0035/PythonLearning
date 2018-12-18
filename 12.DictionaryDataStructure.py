'''
dictionary is the extesnion of set but it store data in form of key value pair
dictionary has same constraint as set that is it can't have duplicates but it is applicable on key value
Set operations like union/intersections/difference is not applicable on dictionary
The value of a key can be anything that is it can be list/iterable
'''
my_friend={
    'Jose':10,
    'Kim':12,
    'Jimmy':5,
    'Jack':2
}
#here the name is the key and no of day is the last seen
"""Accessing dictionary"""
# we can access dictionary using below way
print(my_friend['Jose'])
'''
Here the issue is that when we try to access a value whose key is not present or with different name and we put wrong key to access that
then it will through exception/error so to avoid that we can use dictionary get method
syntex
dic.get("key","Value when not present we can give message")
'''
msg=my_friend.get("Krish","Sorry that value is not present")
print(msg)
print(my_friend)
