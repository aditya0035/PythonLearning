"""
below is the syntex for function with arguments
def <functionName> (<args1>,<args2>,...):
    <function body>
    .......
    .......
    .......
    return <some value/datastructure> #return is not mandatory
    Once we return from function the control goes to caller function
    the scope of variable declared inside function/method is with in that
  
""" 

def functionWithArgs(name):
    print("Hello {0}".format(name))

#function call
functionWithArgs("Aditya")

"""
function with args and return
"""
def functionWithArgsAndReturn(a,b):
    return a+b
    
c=functionWithArgsAndReturn(10,20)
print(c)
