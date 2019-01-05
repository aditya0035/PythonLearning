'''avoid use of default paramters of object type otherwise it will lead and unexpected error like below'''

def account_open(account_name,holder,list_account_holder=[]):
    '''Here there is list will we created and is always associated with method by python and
    the reference of it will not change
    '''
    list_account_holder.append(account_name)
    return {
        "name":account_name,
        "holder":holder,
        "lst_of_holder":list_account_holder
    }

jack=account_open("Jack","Saving")
kim=account_open("Kim","Current")
print(jack["lst_of_holder"])
print(kim["lst_of_holder"])

'''As here we are not passing list but the list contains kim and jack so it might impact functionality'''
'''for object type instead of intializing them we can make None as deafult value for them'''

def account_open_default_none(account_name,holder,list_account_holder=None):
    '''Here there is list will we created and is always associated with method by python and
    the reference of it will not change
    '''
    list_account_holder.append(account_name)
    return {
        "name":account_name,
        "holder":holder,
        "lst_of_holder":list_account_holder
    }

Jimmy=account_open_default_none("Jimmy","Saving",[])
Lilly=account_open_default_none("Lilly","Current",[])
print(Jimmy["lst_of_holder"])
print(Lilly["lst_of_holder"])

'''Default paramter always comes at last before any non default parameter'''
'''in python we can pass parameter as named parameter while calling the method/function'''
