class Currency:
    def __init__(self,money):
        self.money=money
    '''
    def from_sum(self,value1,value2):
        return  value1+value2
    '''
    @staticmethod
    def from_sum(value1,value2):
        return  value1+value2
'''currecny=Currency(12.34)
sum_of_two_value=currecny.from_sum(123.4,15.678)'''
sum_of_two_value=Currency.from_sum(123.44,15.678)
print(sum_of_two_value)

#as here i have to find the sum of two values still i need to cerate instance of the class so what we can do we can
#create static method using @ststicmethod attribute and the function become static not instance so self will remove





