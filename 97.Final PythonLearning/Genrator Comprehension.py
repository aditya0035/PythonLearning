'''like list comprehension there is genrator comprehension'''

gen=(i for i in range(100))
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))