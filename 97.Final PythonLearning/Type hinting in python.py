import typing
'''
Type hinting is used by editors so that we didn't do some wrong typing and get wiered result
although python is still weakly typed language
if we give wrong type python behave as it need to behave
type hinting is just for developer references
args hinted as argsname:typename
and return type is hinted as ->
'''

def type_hinting(name:str,school:str,salary:float,rollno:int)->int:
    print(f'student details are {name}, {school}, {salary}, {rollno}')
    return 12+30

'''we can creat custom type as well like'''
user=dict({str:str,str:int,str:bool})

def custom_type(name:str,school:str)->list(user):
    return None

custom_type("Adity","MIT")
type_hinting("Adity","MIT",123.5,10104)

