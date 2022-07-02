class Item:
    def __init__(self, id, name, value):
        self._id = id
        self.name = name
        self.value = value

    @property
    def ID(self):
        return self._id

class InventoryItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity