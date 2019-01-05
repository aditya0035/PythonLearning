'''genrators are the function which remember there state(previous state) b/w iteration so we can run function
multiple times '''
def hundreaNumber():
    number=[]
    counter=1
    while counter<=100:
        number.append(counter)
        counter+=1
    return number


print(hundreaNumber())
'''
#here we are storing number in list which is going to use memory if we increase
number then memory needed increase
As above the entier list is in memory the genrators remove this kind of risk'''

def hundread_number_genrator():
    print('function called')
    counter=1
    while counter<=100:
        yield  counter
        counter+=1

def hundread_number_without_genrator():
    print('function called')
    counter=1
    while counter<=5:
        print('hi')
        counter+=1

'''so here we have used keyword which is now remember its state from previous execution'''
'''genrators are executed using next() dunder next method '''
'''genrator are not for loop compatable'''

gen=hundread_number_genrator()
'''here calling will return an iterator object so we are able to use next gen'''
'''function return exits immediatly but genartor does not exist their state saved in memmory for further
execution
'''
fun=hundread_number_without_genrator()

'''this will intialize the genrator it will not run the function when we call next on this then it will execute'''
#print(next(gen))
'''in first execution it goes to the function start executing and when reached yield it return value and stop
execution and when we again call next then it will start from where he left that  is form yield 
will increase the counter and again comes to yield and return and wait for next next call
'''
#print(next(gen))
#print(next(gen))
#print(next(gen))