class Animal:
    name=""
    sound=""
    legs=""

    def __init__(self,name,sound,legs):
        self.name=name
        self.sound=sound
        self.legs=legs
    def speak(self):
        print(self.name,"Says :",self.sound,"and has",self.legs,"legs")

dog=Animal("Dog","Woef","4")
cat=Animal("Cat","Moew","4")
horse=Animal("Horse","Neigh","4")
lion=Animal("Lion","Roar","4")
cow=Animal("Cow","Moo","4 ")

dog.speak()
cat.speak()
horse.speak()
lion.speak()