'''in python we can specify the json in both kind of format like an array  conatining dic[{}]
or a dict contains dict
to read a json file we need to import a module name json
both works [{dict obj}] and {dict object}
Json load function give dictinary and dump function convert dict to json string object
we can parse object as json object
when we parse a object as json the json module call dunder repr method that we need to implement in a way that
it return object as JSON

'''
import  json
def json_reading_and_dumping():
    file_pointer=open('demo.json','r')
    content= json.load(file_pointer)
    file_pointer.close()
    print(content)
    '''load Content to python'''
    string='''
    {
    "1": {
      "Name": "Joe",
      "Age": "23",
      "School": "MIT"
    },
    "2": {
      "Name": "Kim",
      "Age": "25",
      "School": "California"
    },
    "3": {
      "Name": "Jimmy",
      "Age": "35",
      "School": "IIT"
    } 
    }
    '''
    file_pointer = open('demo.json', 'w')
    json.dump(string,file_pointer)
    file_pointer.close()


    '''to deal with strings we can use'''
    print("------Deal with string dumps and loads---------")
    print(string)
    new_strings=json.loads(string)
    print("----------")
    print(new_strings)
    string=json.dumps(new_strings)
    print(string)
json_reading_and_dumping()
