"""
DefaultDict is part of collection module
we need to import collection module as its not the part of global module
Whenever we try to access an element using key and if key does not exists then
it will throw error in python but using default dict we can define what to do if
key is not present it never raise a key error also if key is not present it will insert that key with the default value
defined using dictionary factory
"""
from collections import defaultdict
dicts={"Rolf":["MIT",20],"Jose":["California",25]}
defaultdicts=defaultdict(list)
#defaultdicts.default_factory=None #"if none is assign then it will give key error"
for k,v in dicts.items():
    defaultdicts[k]=v

lst=defaultdicts["Kim"]
print(lst)
lst.append("California")
lst.append(25)
print(defaultdicts)

"""
DefaultDict is part of collection module
we need to import collection module as its not the part of global module
Whenever we try to access an element using key and if key does not exists then
it will throw error in python but using default dict we can define what to do if
key is not present it never raise a key error also if key is not present it will insert that key with the default value
defined using dictionary factory
"""
from collections import defaultdict
dicts={"Rolf":["MIT",20],"Jose":["California",25]}
defaultdicts=defaultdict(list)
#defaultdicts.default_factory=None #"if none is assign then it will give key error"
for k,v in dicts.items():
    defaultdicts[k]=v

lst=defaultdicts["Kim"]
print(lst)
lst.append("California")
lst.append(25)
print(defaultdicts)

