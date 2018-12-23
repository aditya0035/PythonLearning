"""
Default value of parameter are assigned using
<varibalename>=default value
Here we have to remeber that when we assign a default value to a list as
parameter for method the python will create a list and associate with that method it will not always
creta a new list
"""
def function_with_default_value(args1=2,args2="Helllo"):
    counter=0
    while counter<args1:
        print(args2)
        counter+=1

function_with_default_value()
print("------------")
function_with_default_value(3)
function_with_default_value(3,"Hello Mr.")

account={
    "saving":150,
    "current":200
}

def add_amount(accountName="saving",amount=130):
    account[accountName]+=amount

add_amount()
print(account)

def CreateAccount(holdername,accounttype,lstOfAccountholders=[]):
    dict={
        "Name":holdername,
        "accounttype":accounttype,
        "holderslist":lstOfAccountholders
    }
    lstOfAccountholders.append(dict)
    return  dict

jose=CreateAccount("Jose","Saving")
print(len(jose["holderslist"]))
kim=CreateAccount("Kim","Current")
print(len(kim["holderslist"]))
print(len(jose["holderslist"]))
"""
As we can see here the list of jose and kim conatins two element that is both are pointing to common
list so to avoid that we can assign these kind of parameter to None
"""