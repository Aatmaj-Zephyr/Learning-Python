class sample:
   rate=3
   def  __init__(self,amount):
        self.amount=amount
   def __init__(self,amount,rate):
       self.amount=amount
       self.rate=rate
   def calculate_tax(self):
       print(self.rate*self.amount*0.01)
mysample=sample(200)
mysample.calculate_tax()
