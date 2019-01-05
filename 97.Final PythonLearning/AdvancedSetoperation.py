set1={1,2,3,4,"Aditya"}
set2={4,"Saraswat","Aditya","aditya"}
print(set1)
print(set2)

print(set1|set2) #union operator
print(set1.union(set2))

#intersection operator
print(set1&set2)
print(set1.intersection(set2))

#difference
print(set1-set2)
print(set1.difference(set2))