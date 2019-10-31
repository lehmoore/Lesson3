from AnimalEncapsulation import *

class Reptile(AnimalE):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None
        self.scales = [True, False]

    def seek_heat(self):
        print("It's cold outside")

    def hunt(self):
        print("Need food")

    def use_venom(self):
        print("Kill them")

CamillaReptile = Reptile()

CamillaReptile.opposable_thumbs()