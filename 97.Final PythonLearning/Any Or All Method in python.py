'''
All check if all the elements in the provided iterables are truthy
if any comes out falsy then All() return false

Any check if any of the element in the provided iterable are truthy
if found then will return truthy

'''

print(all([1,2,3,4,5,6]))
print(all(['',None,0]))
print(any([1,2,3,4,5]))
print(any(['',None,0]))
print(any([['',None,1]]))