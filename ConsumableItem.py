from Item import *

class ConsumableItem(Item):
    def __init__(self, id, name, value, healthModifier):
        super().__init__(id, name, value)
        self.modifier = healthModifier

    def Consume(self, player):
        player.currentHealth += int(self.modifier * player.maxHealth)
        if player.currentHealth > player.maxHealth:
            player.currentHealth = player.maxHealth
        player.inventory.RemoveFromContainer(self)