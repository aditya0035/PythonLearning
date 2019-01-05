'''Iterator in python are the classes/object which have implemented __next__ method in that'''
'''we call genrators from iterator'''
'''range is a kind of iterator with genrator inside it'''
def hundread_number_genrator():
    counter=1;
    while counter<=100:
        yield counter
        counter+=1

gen1=hundread_number_genrator()
gen2=hundread_number_genrator()
print(sum(gen1)) #once genrator execute we can't excute again we have to create new instance
print(list(gen1))
print(list(gen2))
print(sum(gen2))


class hundread_number_iterator:
    def __init__(self):
        self.counter=1
        pass
    def __next__(self):
        if self.counter<=100:
            current= self.counter
            self.counter+=1
            return current
        else:
            raise StopIteration()
            '''the stop iteratin tell python that we reach the end of the iterator'''

gen=hundread_number_iterator()
print(gen.__next__())
print(gen.__next__())
#list(gen) these function does not work on iterator
#sum(gen) these function does not work on iterator

'''as these work on iterable and genrator we need to convert ou iterator to iteratbel'''