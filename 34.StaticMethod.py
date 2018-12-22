"""
Static Method are those which doesnot depends on the object
and they are called using ClassName.StaticMethod
although we can call them from object also
"""
class Foo:
    def __init__(self):
        pass
    @staticmethod
    def hi(self):
        print("Hello i don't like paramter")
        

foo=Foo()
#foo.hi() #can't call like that as it require a parameter
Foo.hi(foo)
