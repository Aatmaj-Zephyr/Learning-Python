class sample:
   def  __init__(self):
        print("Class instantiated")
   def fun(self):
       self.__init__()
       print("inside a function")
mysample=sample()
mysample.fun()
