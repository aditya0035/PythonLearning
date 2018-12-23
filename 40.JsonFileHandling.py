"""
there are two ways to json
{
    "<KeyName>":[{dict},{dict}]
}
{
    [
    {dict},
    {dict}
    ]
}
with out key or with key python can deal will any of this
python have built in module for dealing with this its not global module so we need to import that
import json
the method are 
json.dump() it will put the data into json file provided using filepointer
json.loads() it will load the data into a python variable which is of type dict
json.loads() it will load the octent of json string into a variable of dict type
json.dumps() it will load the content  of dict type into a string variable
"""
import json
filePointer=open("JsonFile.json","r")
content=json.load(filePointer)
print(content)

"""
When we parse an object to JSON we need to implement the __repr__ method which should return the json string
"""