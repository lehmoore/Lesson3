from AnimalInheritance import *

class Reptile(AnimalI):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("It's cold outside")

    def hunt(self):
        print("Need food")

    def use_venom(self):
        print("Kill them")

JeremyReptile = Reptile()
JeremyReptile.hunt()

# print(JeremyReptile.eat()) would return Yum and None because there is already a print function within the original
# code. Where there is no print function use print. If you want to use print(JeremyReptile.eat()) then use return
# within the original code instead of print.