class animal:
 food=""
 def makenoise(Self):
     pass
 
class pet():
    def bepetted(self):
        print("Pet me")

class canine():
    def shownails(self):
        print("My nails are long")
        
class dog(pet):
    def __init__(self):
        print("I am a dog")
        self.food="bone"
    def makenoise(self):
        print("Woof!")

class cat(pet,canine):
    def __init__(self):
        self.food="milk"
        print("I am a cat")
    def makenoise(self):
        print("meow!")
        
Tommy=dog()
Tommy.makenoise()
Tommy.bepetted()
print(Tommy.food)
Dina=cat()
Dina.shownails()
Dina.bepetted()
print(Dina.food)
