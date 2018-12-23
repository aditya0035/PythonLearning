"""
in python we use two keyword for argument unpacking
* and **
* unpack the argument based on index and ** unpack the argument base on keyword
"""

def function(a,b,c):
    print(a+b+c)

tuple=(10,12,15)

function(a=tuple[0],b=tuple[1],c=tuple[2])
function(*tuple) #here it is equivalent to a=tuple[0],b=tuple[1],c=tuple[3]

dicts={"a":10,"b":12,"c":15}
"so here we can call the function as"
function(a=dicts["a"],b=dicts["b"],c=dicts["c"])
"here the same is achieve using **"
function(**dicts) #here it will do the same

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

lst_of_user=[{"name":"Jose","age":30},{"name":"Kim","age":25}]
user_obj_list=[User(**args) for args in lst_of_user]
print(user_obj_list)