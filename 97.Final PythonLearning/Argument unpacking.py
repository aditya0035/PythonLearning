account={
    "saving":200.0,
    "checking":150.0
}
def add_balance(name,amount):
    account[name]+=amount
    return  account[name]

'''Here if we have to do only one or two transaction then we will do as below'''
print(add_balance("saving",200.0))
print(add_balance("checking",150.0))

'''what we will do if we have like this'''
transactions=[
    ('saving',-180.0)
    ('checking',200)
    ('saving',800)
    ('cehcking',200)
]

'''there are various way to do it'''
for name,amount in transactions:
    add_balance(name,amount)

'''another way is'''
for tuple_obj in transactions:
    add_balance(tuple_obj[0],tuple_obj[1])

'''this can be written as'''
for t in transactions:
    add_balance(name=t[0],amount=t[1])

'''here instead of doing this we can do like that argument unpacking'''
for t in transactions:
    add_balance(*t)
'''argument unpacking is done using * and here it will map like that name=t[0] and amount=t[1]'''

print(account["saving"])
print(account["checking"])
