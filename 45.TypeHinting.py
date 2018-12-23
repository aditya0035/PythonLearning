from typing import Dict
from typing import List
from typing import Union

lstOfPerson=List[Dict[str,Union[str,int]]]

def Typeing_Method(age:int,name:str)->str:
    return "Hello"

def TyeeFunction()->lstOfPerson:
    return [{"Age":30,"Name":"Aditya"}]

print(TyeeFunction())

"""
Type hinting does not alter python workig behaviour that is python will be still weak type language
but it help the developer to developer application with less error prone
""" 