class animal:
 food=""
 def makenoise(Self):
     pass
 
class pet():
    habitat="home"
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
class wild(animal):
    habitat="Jungle"
    
class tiger(canine,wild):
    def __init__(self):
        self.food="meat"
        print("I am a tiger")
    def makenoise(self):
        print("Grrr.!")
Tommy=dog()

Dina=cat()

Tigo=tiger()

for i in (Tommy,Dina,Tigo):
    print(i.food)
    i.makenoise()
    try:
        i.shownails()
    except:
        pass
    try:
        i.bepetted()
    except:
        pass
    print(i.habitat)
