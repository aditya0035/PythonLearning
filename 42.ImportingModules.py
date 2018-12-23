"""
In python we use import keyword to import a module(python file)
in our program
like
import json
import JsonFileHandling

when we write it in this way it will execute the module so if there is block which is in main scope will execute
but here the module is not run as __name__="__main__"

sometimes we give like this
from json import load
it will import specific function load from json,in this case it will execute the module and will create a dictionary and from that dictioanry it
will return load this type of import can lead to circular dependency so be aware while doing this
from json import *
it will import all function and will create dict of function and content

__name__ is a python path variable when we run a program then it will set __name__ to __main__ for that program
if import statement contains any relative path all the relative path are determined on this basis so 
be careful while using relative path

below are the realtive path
1.Relative import children(.)
from .xyz.lmn.json import function
here if we run the package from top level and from parent we are calling this child then it will work as 
for parent module it will set __name__ variable to the parent path
and then attach that variale to relative path to find the child module
but if i run parent modules as main then it might give error as now __name__ will __main__ so it will append that name and will lookout for that

2.Relative Import Parent(.. two dot)
as . represent current directory so .. will move from that directory to one level up
so here the same problem may arise if we run child module as main and its referring parent mdoule using relative path then it will
look for __main__ with upper level which does not exits

problems with import circular import
"""

'''
In each folder we can have __init__.py file it will call wheever we import a module from the directory 
so it can be used to put common variable or values which might be used by other modules as well
'''