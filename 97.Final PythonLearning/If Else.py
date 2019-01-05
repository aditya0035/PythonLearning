age=input("Please provide your age \n")

if int(age)>=18:
    print("You are adult")
else:
    print("you are not adults")

if int(age)<18:
    print("you are minor")
elif int(age)>=18 and int(age)<60:
    print("you are teenager")
else:
    print("you are senior citezen")
