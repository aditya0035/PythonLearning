"""
We can use python Generator like python thread
as we know that when w yield a  function it suspend its execution
So the basic principle of threading is genreator
"""
def countdown(n):
    counter=0
    while counter<=n:
        yield counter
        counter+=1


c1=countdown(10)
c2=countdown(12)

"""
If i run c1 then c2 like this
"""
print(next(c1))
print(next(c2))
print(next(c1))
print(next(c2))
"""
It is the way the threading works in python this is basic of Async Programming in generator
"""
"""
Although we can create own task Schedular
"""

Tasks=[countdown(10),countdown(12),countdown(14)]

while Tasks:
    task=Tasks[0]
    Tasks.remove(task)
    try:
        print(next(task))
        Tasks.append(task)
    except StopIteration:
        print("Function Execution End")



