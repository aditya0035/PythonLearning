"""
ABC stands for Abstract base class
there is no concept of interface in python although we can restrict the python
to make the instance of a class like Vehicle.
and such classes are called abstract class
and they can have a abstract method abstract methods are those which has signature but no body
they need to be implemented in child class

for ABC we need to import ABC module
"""
from abc import ABCMeta,abstractmethod
class Animal(metaclass=ABCMeta):
    def DoSomething(self):
        print("Do Something")
    @abstractmethod
    def abstractMethod(self):
        pass

animal=Animal()
animal.DoSomething()
