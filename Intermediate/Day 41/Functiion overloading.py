class sample():
 a=2
 b=3
 def __init__(self):
     self.a=100
     self.b=50
 def fun(self):
     print("Hello world")
     
     
class sample2(sample):
    def __init__(self):
     super().__init__()
    def fun(self):
        print(self.a+self.b)
        
mysample2=sample2()
mysample2.fun()

