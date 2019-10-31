# POLYMORPHISM refers to the ability of an object to adapt the code

from EncapsulationReptile import *

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        return "Do I say it smells or tastes nice..?"

Sidney = Snake()
Sidney.seek_heat()

Simon = Snake()
print(Simon.use_tongue_to_smell())