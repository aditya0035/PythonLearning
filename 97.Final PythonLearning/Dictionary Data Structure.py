'''dic is the extesnion o  store data in key value pair and does not support set operation'''
my_friends={
    'joe':4,
    'jack':10,
    'rose':14,
    'Raj':None
}

#key can't be duplicate and can be any datatype
#Accesing Dict
print(my_friends["joe"])
# print(my_friends["jimmy"])  error as key is not present so avoid this wecan use get function like
print(my_friends.get("jimmy","Key not exists"))

print(sum([1,2,3,4,5]))
print(len(my_friends))
#dic store data in the form of dict_items which is array of tuple
dict_items=my_friends.items()

diciterator=dict_items.__iter__()

k,v=next(diciterator)
print(f"Key:{k},Value:{v}")
for k,v in dict_items:
    print(f' Key:{k},Value:{v}')
