class First(object):
    def __init__(self):
        print ("first")

class Second(object):
    def __init__(self):
        print ("second")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__() #in python 2.0 version
        print ("that's it")


third=Third()

"""
In this example, Third() will call 
First.__init__. 
Python looks for each attribute in the class's parents as they are listed left to right. 
In this case we are looking for __init__. So, if you define

class Third(First, Second):
    ...
Python will start by looking at First, and,
 if First doesn't have the attribute, then it will look at Second.

This situation becomes more complex when inheritance starts 
crossing paths (for example if First inherited from Second). 
 but, in a nutshell, 
 Python will try to maintain the order in which each class appears on the inheritance list, 
 starting with the child class itself.

So, for instance, if you had:

class First(object):
    def __init__(self):
        print "first"

class Second(First):
    def __init__(self):
        print "second"

class Third(First):
    def __init__(self):
        print "third"

class Fourth(Second, Third):
    def __init__(self):
        super(Fourth, self).__init__()
        print "that's it"
the MRO would be [Fourth, Second, Third, First].

By the way: if Python cannot find a coherent method resolution order, it'll raise an exception, instead of falling back to a behaviour which might surprise the user.

Edited to add example of an ambiguous MRO:

class First(object):
    def __init__(self):
        print "first"

class Second(First):
    def __init__(self):
        print "second"

class Third(First, Second):
    def __init__(self):
        print "third"
Should Third's MRO be [First, Second] or [Second, First]? There's no obvious expectation, and Python will raise an error:

TypeError: Error when calling the metaclass bases
    Cannot create a consistent method resolution order (MRO) for bases Second, First
"""
