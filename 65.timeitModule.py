"""
for performance we can use datetime module time class time.time()
but there is another module to log the time of execution of a block
of code and it is timeit which we need to import that
"""
import  timeit
log_time=timeit.timeit("[x*2 for x in range(50)]")
"""
Here timeit will run that module to 1000 times and will calculate the average of that 
"""
print(log_time)"""
for performance we can use datetime module time class time.time()
but there is another module to log the time of execution of a block
of code and it is timeit which we need to import that
"""
import  timeit
log_time=timeit.timeit("[x*2 for x in range(50)]")
"""
Here timeit will run that module to 1000 times and will calculate the average of that 
"""
print(log_time)