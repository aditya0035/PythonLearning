import re
string='My 2 Favorates Numbers are 19 and 42'
print(string)
y=re.findall("[0-9]+",string)
print(y) #here it will extract data from string 2,19,42

#string start with implementation using search

x="From:Aditya ..........."
if re.search("^From",x):
    print("Match Found")

y="Start With XYZ"
if re.search("With",y):
    print("Match Found")

"Split function Implementation Using Regex"

commaSepratedString="Aditya,MIT,30"
lstOfString=re.findall("([A-z 0-9 \s]+)",commaSepratedString)
print(lstOfString)


"""
Greedy Matching
"""
x="From:Using the:Character"
y=re.findall("^F.+:",x)
print(y) #here it produces the output as greedy as there are two possible strings to fecth
"""
['From:Using the:'] 
['From:']
but here it has fetched ['From:Using the:']  so these * and + are greedy regex character 
as in regex if we didn't say anything the regex lib attempt to give the largest possible version of the string
so to fix that to non greedy search we can use +?,*? which make us to give the first matched string
"""
y=re.findall("^F.+?:",x)
print(y)

email="from:stephan.marquard@uct.ac.za"
y=re.findall("^from:(\S+@\S+)",email) 
#here it will gives the group value as output the parentheses are not the part of match but they tell where to start and
#end in order to extract the string
print(y)

"""
Double Split pattern
Sometimes we split a line one way then grasp one of the piece of the line and split that piece again
Escape Character:
if we want a special regular expression character to just behave normally then we have to prefix that with \ character
"""
