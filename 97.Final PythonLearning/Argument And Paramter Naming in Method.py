class Movie:
    def __init__(self,name,year):
        self.name=name
        self.year=year
movies=Movie("The Matrix","1994")
print(movies.name)
'''we can put object in data structures'''

'''Object are conceptualization of entities'''

'''Magic Method in python'''
print(movies.__class__)
print(__name__)
print("Hi".__class__)