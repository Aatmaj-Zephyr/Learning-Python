class ape():
    food=""
    def __init__(self,weight):
        self.weight=weight
    def cry(self):
        pass # Do nothing
    def eat(self):
        print(self.food)
        
class chimpanzee(ape):
    def __init__(self,weight):
        super().__init__(weight)
        self.food="bananas"
    def cry(self):
        print("I am a chimp")

class gorrilla(ape):
    def __init__(self,weight):
        super().__init__(weight)
        self.food="fruits"
    def cry(self):
        print("I am a gorrilla")
  
class gorranzee(chimpanzee,gorrilla):
    pass

A=gorranzee(20)
print(A.food)
A.cry()
