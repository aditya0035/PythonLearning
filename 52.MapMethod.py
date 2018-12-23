numbs=[2,3,5,6,87,9]
mapped_num= map(lambda x:x*2,numbs)
print(type(mapped_num))
print(list(mapped_num))
"Map function return a generator"
"""
we can replace the map function with generator 
"""
mapped_num=(x*2 for x in numbs)
print(list(mapped_num))

"""
When we run both the generator will execute faster if function is not predefined and a lambda is used 
for map
"""numbs=[2,3,5,6,87,9]
mapped_num= map(lambda x:x*2,numbs)
print(type(mapped_num))
print(list(mapped_num))
"Map function return a generator"
"""
we can replace the map function with generator 
"""
mapped_num=(x*2 for x in numbs)
print(list(mapped_num))

"""
When we run both the generator will execute faster if function is not predefined and a lambda is used 
for map
"""