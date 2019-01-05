friends={'Rolf','Anna','Charlie'}
friends_lower={friend.lower() for friend in friends}
print(friends)
print(friends_lower)

#dic comprehension
lst_friends=['Rolf','Anna','Charlie','Jack']
lst_last_seen=[2,6,1,10]

#1st way
dict_friends={lst_friends[i]:lst_last_seen[i] for i in range(len(lst_friends))}
print(dict_friends)

#2nd way
print(dict(zip(lst_friends,lst_last_seen)))

print(next(zip(lst_friends,lst_last_seen,friends))) #zip function create a tuple with provided iterables Zip is genrator

