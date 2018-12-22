set1={i for i in range(5)}
set2={i for i in range(4,9)}
print(set1)
print(set2)
set3={ i for i in set1 if i not in set2}
print(set3) #difference of sets
set4={i for i in set1 if i in set2}
print(set4) #intersection of sets
set5={i for i in (set1 | set2)}
print(set5)

'''
Set are useful for matching or non matching of elements
'''
