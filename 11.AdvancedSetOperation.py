set_one={1,2,3,4,5}
set_two={4,5,6}
#Intersection of set that is common amoung both set i.e. 4 & 5 in this case
print(set_one & set_two) # & is used for intersection
print(set_one.intersection(set_two)) # we can use intersection set module also

#union of set that is will fetch all the value which are not in 1st set but are in 2nd that all data
print(set_one)
print(set_two)
print(set_one|set_two) # pipe | is used for union 
print(set_one.union(set_two)) #we can use set union method also for getting union

#difference of set means that it will provide the data which is on the first set/Caller Set not in 2nd set it will remove common and return remaining
print(set_one-set_two) #we can use - to fetch the difference of sets
print(set_one.difference(set_two)) # we can also use the difference method of set