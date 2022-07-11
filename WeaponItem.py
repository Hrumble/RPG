from Item import *

class WeaponItem(Item):
    def __init__(self, id, name, value, damage, slot = "hand", craftable = True):
        super().__init__(id, name, value, craftable)
        self.damage = damage
        self.slot = slot
        self.type = "Weapon"

    def ExtraInfo(self):
        print(f"DMG: {self.damage}")
