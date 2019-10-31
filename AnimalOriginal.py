# FOUR PILLARS OF OBJECT ORIENTED PROGRAMMING
# 1 - Abstraction
# 2 - Inheritance
# 3 - Encapsulation
# 4 - Polymorphism

# ABSTRACTION means hiding the complexity and showing the essential features of the object.
#
class Animal():

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def eat(self, food):
        return "I ate " + food + " and it was good"
    def sleep(self):
        return "Zzzzzz"

