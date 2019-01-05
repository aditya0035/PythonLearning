Users=[
    {"username":"abc","password":"123"},
    {"username":"lmn","password":"123"}
]

class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def __repr__(self):
        return f"[<User Class>:Username={self.username}, Passowrd={self.password}]"

lst_of_user_obj=[]
for user in Users:
    lst_of_user_obj.append(User(username=user["username"],password=user["password"]))
print(lst_of_user_obj)
'''this whole thing above can be done using key unpacking'''
del lst_of_user_obj
lst_of_user_obj=[User(**user) for user in Users]

'''key unpacking is done using **variale as it done as key=variables[key]'''
print(lst_of_user_obj)
