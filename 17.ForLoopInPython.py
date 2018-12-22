"""
For loop allow us to iterate over iterables
"""
for i in range(6):
    print("{0}".format(i))

my_friends = ["Jose", "Jack", "Jim"]
for friend in my_friends:
    print(friend)

for i in range(0, 5):  # here 0 is inclusive and 5 is exclusive
    print(i)
print(type(range))

"""
Iterate over dictionary 
when we iterate over dictionary using for loop it gives use a key
but when we iterate over dictionary using dictionaryobject.items()
it is a object which is array of tuples which contains key and value of dict
so it returns a tuples
"""
my_friends_dict={
    'Aditya':10,
    'Abdul':14,
    'Salil':0,
    'Devashish':5,
    'Shantanu':10
}
print(my_friends_dict.items()) #array of tuples
for key in my_friends_dict:
    print("Key:{0},Value:{1}".format(key,my_friends_dict[key]))
    
a,b=(10,15)
print("a:{0},b{1}".format(a,b)) #this is called tuple destructuring

for key,value in my_friends_dict.items():
    print("key:{0},value:{1}".format(key,value))
