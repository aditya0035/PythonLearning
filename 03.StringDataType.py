'''string datatype is a sequence of character  '''
'''We can perfom range operators on string like [::]'''
'''[start:end:diff] is a range operator which can provide substring'''
'''Here start is the index form where to start default it is zero'''
'''Here End is the index where to go is nothing then till end'''
'''Diff is the gap which we have to leave'''
'''Here StartIndex is inclusive and end index is exclusive'''
''' string='Aditya' here A's index is 0 as python is zero index based Index 
            012345 these are all the index of the string character
          -6-5-4-3-2-1 these are all the negative index of the string character
The Range Operator works with negative index but it run form left to 
right direction always           
'''
string = "NORWEGIAN BLUE"
print(string[:5])
# here it will give string starting from 0(inc) to 5(excl) NORWE

print(string[1:])
# here End Index is not given so default is to end ORWEGIAN BLUE

print(string[1:7:2])
# here it will give string with 2 char gap b/w them OWE

print(string[0:-4]) 
# here it will go from 0 to neative form left to right NORWEGIAN 

print(string[-6:-2])
# here it will start from A till y(excl) N BL

print(string[-1])
# it will give last character of string which is E

