"""
Use for Async Development
it is a function which remember its state in b/w execution so we can run a function muliplle times
and it will remember its state b/w last execution so when we call it again it start from there
"""
def GenrateNumber(n):
    counter=0
    nums=[]
    while counter<=n:
        nums.append(counter)
        counter=counter+1
    return nums

print(GenrateNumber(100))
"""
Here the above function will generate the number to 100 will it will
save them in 100 mememory location each for one number which is quite costly
also here we didn't need the number in one go
So here the generator will comes into play
"""
'''
Here when we call generator they provide us the first element and then yield the function state in
memory then when we call next time it start executing from where we left and yield the next result
and so on
'''
"""
How to Create Generator
"""
def Generator(n):
    counter=0
    while counter<=n:
        yield counter
        counter+=1

"""
to call a generator first we need to intilize the generator
"""
g=Generator(100)
#then when we call the next on generator it will execute the function and yield the first
#output provided and then save the state for next call

#here it will not generate all the no in one go so quite memory efficient

print(next(g))
print(next(g))

"""
Generator will bw helpful when we want to stop a function temparly and call next() to function 
execute our function

range(10) function will behave like generator but these are not generator
"""

lst=list(g) #it will create a list from the generator
print(lst)