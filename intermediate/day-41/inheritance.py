class sample():
 a=2
 b=3
 def fun(self):
     print("Hello world")
     
class sample2(sample):
    def fun2(self):
        print(self.a+self.b)
        
mysample2=sample2()
mysample2.fun()
mysample2.fun2()
