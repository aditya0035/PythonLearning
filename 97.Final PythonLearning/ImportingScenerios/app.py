import ImportingScenerios.utils.find #this is call absolute export

'''
There are two ways to run python file
1.as a main script
2.as a module
when we run a python file as main script the dunder name variable is set to __main__
and then it will search for all module based on that
if we provide a absolute path then there is no issue but if 
we provide a relative path then there is a issue and we have to make sure that __name__ variable
set is correct and able to locate imported path

When we write 
import xyz
it will run whole module and create a dict

from xyz import lmn
here it will run whole module and create a dict(this dict is create only one time)
so the module executed one time and then it search on that function so it might create circular dependency
'''
'''
from parent to child namespace mapping relative we use single dot(.)
from child to parent namespace mapping we use double dot(..)

so it is good if we want to run some code when the module is run as main module put your code inside
if __name__='__main__'

when a module is run as script the name is set to __main__
the module search is done based on __name__ variable value and its value varies form module to module

__init__.py file is always executed when ever we import or run a module as script 
it is used to declare certain variable which might be used throughout all the modules in the directory
'''
def app_operation():
    print("app")

print(__name__)