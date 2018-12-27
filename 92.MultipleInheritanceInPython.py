"""
In python we can inherit multiple class
"""

class A(object):
    def __init__(self):
        print("Entering A")
        print("Leaving A")

class B(object):
    def __init__(self):
        print("Entering B")
        print("Leaving B")

class C(A, B):
    def __init__(self):
        print("Entering C")
        A.__init__(self)
        B.__init__(self)
        print("Leaving C")


c=C() #here we did calling which is old style now we can call using Super keyword lie

#this is followed when we have different classe as we can't call using super



"""
In python we can inherit multiple class
"""

class A(object):
    def __init__(self):
        print("Entering A")
        print("Leaving A")

class B(object):
    def __init__(self):
        print("Entering B")
        print("Leaving B")

class C(A, B):
    def __init__(self):
        print("Entering C")
        A.__init__(self)
        B.__init__(self)
        print("Leaving C")


c=C() #here we did calling which is old style now we can call using Super keyword lie

#this is followed when we have different classe as we can't call using super



