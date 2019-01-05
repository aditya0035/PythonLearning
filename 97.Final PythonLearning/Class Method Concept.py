class Currency:
    def __init__(self,value):
        self.value=value
    def from_sum(self,value1,value2):
        return  Currency(value1+value2)
    def __repr__(self):
        return f"Currecny:{self.value}"

class DollerCurrecny(Currency):
    def __init__(self,value):
        super().__init__(value)
        self.CurrencyCode='$'

dollerAmount=DollerCurrecny(12.45)
sum_of_value=dollerAmount.from_sum(1345.5,13456)
print(type(sum_of_value))

'''As here it is returning Currency but the object we are reffering is Dollar so one way is to Override the method'''
'''Another approch is we can make this method as class method'''

class Amount:
    def __init__(self,value):
        self.value=value
    @classmethod  #here the cls keword is used for class call
    def from_sum(cls,value1,value2):
       return cls(value1+value2)

    def __str__(self):
        return f"Amount is:{self.value}"

class DollarAmount(Amount):
    def __init__(self,value):
        super().__init__(value)
        self.currecnycode='$'
    def __str__(self):
        return f"Amount is {self.currecnycode} {self.value}"

dollerAmount=DollarAmount(12.34)
print(dollerAmount.from_sum(12.34,13456.7))


