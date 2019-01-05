'''
filter method takes a function and an iterable it return the filtered value
the provided function should return true or false value
'''

friends=["Jack","Joe","Jimmy","Charlie","Kim","Chales"]
closed_friends=["Jack","Joe"]

print(list(filter(lambda x:x not in closed_friends,friends)))
'''filter method return a genrator'''
gen=(person for person in friends if person not in closed_friends)
print(list(gen))

'''
Filter execute faster if the function is already defined but if not then genrator comprehension run faster
order of execution
filter with function>genartor comprehension>filter with lambda
'''