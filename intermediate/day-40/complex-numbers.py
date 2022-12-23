class Complex:
    #Default values
    x=0
    y=0 

    def __init__(self,x,y):
        self.x=x
        self.y=y
    def absolute(self):
        return (self.x**2+self.y**2)**0.5

a=Complex(2,-3)
print(a.absolute())
b=Complex(4,5)
print(b.absolute())
