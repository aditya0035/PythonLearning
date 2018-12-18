'''
These act as dicision making statement
'''
is_programmer=input("Are you a progammer Please give in Yes/No")
if is_programmer=="Yes":
    print("you are awasome")
else
    print("You can be awasome")
is_student=input("Are you a student please provide Yes/No")
if is_programmer=="Yes" and is_student=="Yes":
    print("You are awasome")
elif is_programmer=="No" and is_student="Yes":
    print("You are good")
else:
    print("You need to learn some language")

print("End") #it is not part of else due to indentation level as python highly work on indentation language as its iterpreter language
"""
We can directly check for object like 
if is_programmer:
    print("you are awasome")
as here is_programmer will be a value otherwise None which is treated as False
  
""" 