"""
Similaraly like len()function there are two function which work on iterable/iterator/genrators.
1.sum
2.list
"""
my_list=[1,34,56,78,90]
print(sum(my_list))
"""
Here it will add all element of the iterable and provide the sum
"""
"""
list() function genrate list from the iterator/genrators/iterables
"""
print((range(1, 50)))
print(list(range(0, 50)))

def genrator(number):
    counter=0
    while counter<number:
        yield counter
        counter+=1
        

g= genrator(10)
lst=list(g)
print(lst)