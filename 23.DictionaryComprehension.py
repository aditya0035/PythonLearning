my_list_friends=["Aditya","Anuj","Jose","Jack","Jim"]
my_list_noOfDays=[10,5,4,3,7]
# 1st way
my_list_dict={my_list_friends[i]:my_list_noOfDays[i] for i in range(len(my_list_friends))}
print(my_list_dict)

#2nd way
my_list_dict={ value:my_list_noOfDays[index] for index,value in enumerate(my_list_friends)}
print(my_list_dict)

#3rd way
my_list_dict=dict(zip(my_list_friends,my_list_noOfDays))

#zip function genrate a list of tuple contains elements from the iterable mentioned
#dict() function mtakes array of key value pair of that to create a dictionary
print(my_list_dict)
print(zip(my_list_friends, my_list_noOfDays))
print(next(zip(my_list_friends,my_list_noOfDays)))