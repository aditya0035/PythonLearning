string="Hello"
# string is sequence of characters which does not have nay meaning to computer but for human it has
# Accessing string using index for that string has implemented __getItems__ dunder method
# python follow zero based index concept
print(string[2])
# string in python are immutable
# string[2]="a"
# Negative index concept string
print(string[-1])    # H E L L O
                     # 0 1 2 3 4
                     # -5 -4 -3 -2 -1
print(string[-4])
print(string[-5])

#range operator
print(string[0:]) #return whole stringS
print(string[1:]) #return string from index 1 to last
print(string[1:4]) #return string starting from 1(inclusive) to 4 index(Exclusive)
print(string[-1:-3]) # no result as work from left to right
print(string[-5:-1])

#format string
print("Hello Mr.{} {}".format("Aditya","Saraswat"))
print("Hello Mr.{firstname} {lastname}".format(firstname="Aditya",lastname="Saraswat"))

#post python 3 use this
firstName="Aditya"
lastName="Saraswat"
print(f'Hello Mr. {firstName} {lastName}')

