import timeit
print(timeit.timeit("[x**2 for x in range(10)]"))

print(timeit.timeit("map(lambda x:x**2,range(10))"))