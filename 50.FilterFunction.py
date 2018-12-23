"""
its a global function it filter the result based on provided condition if that comes true
filter() function takes two argument 1.Filter function which will return true/false
2.the iterable
"""
friends=["Rolf","Jose","Randy","Anna","Mary"]
def StartWithR(friend:str):
    return str.startswith(friend,'R')
filter_list=list(filter(StartWithR,friends))
print(filter_list) 
"""
Filter method returns a generators
it keep those element for which the filter function return true
"""
friends=["Rolf","Jose","Randy","Anna","Mary"]
another_list=(friend for friend in friends if friend.startswith('R'))
print(list(another_list))
"""
Above is using the generator comprehension and it run  faster then filter function

when we use lambda remeber that return value should be an expression
"""