# INHERITANCE allows us to define a child class that inherits all the methods and properties from a parent class

class AnimalI:

# Defining the attributes

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in and one breath out")

    def eat(self):
        print("Yum")

    def move(self):
        print("Just keep swimming")
