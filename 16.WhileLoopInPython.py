'''
While allow to run a block of code to a number of times based on the provided boolean condiion,
it execute till the condition is true
'''
while True:
    user_input = input("Did you learn a language");
    if user_input == 'Y':
        print("You are awsome")
        break
    else:
        continue

"""
break statement is used for existing from loop
continue skip the statement below it and execute the next loop iteration
While loop can be used to iterate over a number of time as below
"""
counter=1
while counter<=10:
     print(f'counter value is {counter}')
 counter+=1
