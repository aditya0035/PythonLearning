'''
When a function call itself from its body it is called recusive function 
below are the rule for recursive functions
1.it should contains atleast on block which will exit the function after a certain condition reach
2.It should ontains a block which will call the function
'''
#example of recursive function is factorial
'''
e.g. 5!=5*4*3*2*1
e.g. 0!=1
e.g. 1!=1
eg. 4!=4*3*2*1
'''

num_dict={}
def factorials(n):
    if n in (0, 1):
        return 1
    else:
        if num_dict.get(n-1,None)!=None:
            return n* num_dict.get(n-1)
        else:
            num_dict[n-1]=factorials(n-1)
            return n*num_dict[n-1]
            

factorials(5)
#instead of tha we can do this also we can travel from end to avoid stack overflow error
            

