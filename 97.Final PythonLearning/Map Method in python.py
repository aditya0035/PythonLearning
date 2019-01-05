'''map method takes two args 1st is the function which is going to provide new values based on some
logic and second is the iterables map provides a generator'''
gen=map(lambda x:x**2,[i for i in range(1,100)])
print(list(gen))
