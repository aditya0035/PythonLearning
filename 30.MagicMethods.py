"""
Megic method are those method which are in built method we just provide
implementation for them as everything in python is an object
"""
class Garage:
    def __init__(self,brand):
        self.brand=brand
        self.cars=[]
    def __len__(self):
        return len(self.cars)
    def __getitem__(self,index):
        return self.cars[index]

ford=Garage("Ford") #this is the garage of ford
ford.cars.append("Fiesta")
ford.cars.append("Focus")
# Now i want to know how many cars are there in ford garage
print(len(ford)) #error:TypeError: object of type 'Garage' has no len()
"""
To Resolve this error we need to implement __len__(dunder length) magic method in Garage class
Then when we call len(object) over that it will work
"""
print(len(ford))

#Now i want to see which are all the cars in ford garage ,for that we need to iterate over ford garage 
for car in ford:
    print(car) #TypeError: 'Garage' object is not iterable

#ford[1] TypeError: 'Garage' object does not support indexing

"""
So to resolve these two error we need to implement __getItem__ method in the class 
ford[1] internally python call Garage.__getitem__(ford,1)
So as we have implemented both __len__ and __getitem__ so we are able to iterate that object over for loop
"""
