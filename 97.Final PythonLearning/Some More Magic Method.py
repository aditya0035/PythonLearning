class Garage:
    def __init__(self):
        self.cars=[]

    def __repr__(self):
        return  f'garage has {len(self.cars)} cars'
    def __str__(self):
     # this will something information about the object
        return str(self.__class__)
    def __add__(self, other):
       return self.cars+other.cars
    def __iadd__(self, other):
        return self.cars+other.cars
garage=Garage()
garage.cars.append("Ford")
print(garage)

'''to print more about object we are going to implement __repr__ method dunder repr method'''

'''repr method print string represntation of objet'''


garage1=Garage()
garage1.cars.append("Ford")
garage2=Garage()
garage2.cars.append("Benz")
garage1.cars+=garage2.cars #here it will call iadd
garage2.cars=garage2.cars+garage1.cars # here it will call add
print(garage1.cars)
print(garage2.cars)

#differnece b/w iadd and add is that add return new object while iadd modify the same object not valid on primitive type
#similarly for add we can over ride sub,multiplication,division ,modulous etc
