# ENCAPSULATION is the internal representation of an object that will not be shown to the user.
# Basically just use an underscore and then it will be hidden and won't be usable when imported in to other files.
# The stuff below is using inheritance again not anything to do with encapsulation.

class AnimalE:

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

    def opposable_thumbs(self):
        print("I declare a thumb war!")