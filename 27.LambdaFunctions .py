'''
lambda functiona are also known as annoynymous function
we can although can create lambda method with named one
syntex of lambda
lambda : <return statement>
lambda (args1...):<return statement>
lambda(ags1,agrs2):<return statement>(val1,value2) #immediate lambda function call
lambdafunction=lambda(agrs1):<return statement> #named lambda function
lambdafunction(12)
'''
greet=lambda:print("Welcome to the python") #named lambda
greet()

#direct call lambda function()
c=(lambda a,b :a+b)(10,12)
print(c)