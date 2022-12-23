class sample:
    rate=15

    def set_amount(self,amount):
        sample.amount=amount
    def print_tax(self,amount):
        self.set_amount(amount) 
        # Exercise why not self.set_amount(self,amount) ?
        print(self.rate*self.amount/100)
        
    
a=sample()
a.print_tax(20)
