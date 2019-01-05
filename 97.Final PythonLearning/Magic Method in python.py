'''In this will explain magic method'''
class Garage:
    def __init__(self):
        self.cars=[]
    def __len__(self):
         print("from garage")
         return  len(self.cars)
    def __getitem__(self, index):
        return self.cars[index]
garage=Garage()
garage.cars.append("Fiesta")
garage.cars.append("Ford")
garage.cars.append("Zipsi")

print(len(garage)) # here to do that we need to implement __len__ method in the class
print(garage[0]) #TypeError: 'Garage' object does not support indexing to resolve this and
                    # enabling indexing on class we need to implement __getitem__

for car in garage:
    '''Note:to iterate over for the class need to implement __len__ and __getitem__ dunder method'''
    print(f'car:{car}')
