class sample:
    rate=15

    def __set_amount(self,amount):
        sample.amount=amount
    def print_tax(self,amount):
        self.__set_amount(amount) 
        print(self.rate*self.amount/100)
        
    
a=sample()
a.__set_amount(2)
a.print_tax(20)
