'''
for finding the length of any iterable like list,set,dic,tuple we can use len() function which will give the length of
iterable as count of number of the element in the iterable
'''
"""
Note:-actualy we are able to find length from any implemented class even though from our own class for that we have to 
implement the __len__ (dunder length) function in our class which will return a numeric value
"""
friend_list=["Aditya","Jose","Jack","Jim"]
print(len(friend_list))
friend_tuple=("Aditya","Jose","Jack","Jim","kim")
print(len(friend_tuple))
friend_set={"Aditya","Jose","Jack"}
print(len(friend_set))
friend_dict={"Jose":0,"jack":12,"kim":None}
print(len(friend_dict))

class CustomLength:
    def __init__(self):
        pass
    def __len__(self):
        return 10

customClass=CustomLength()
print(len(customClass))