from entity.menu.item import Item

class Menu:
    _items: list

    def __init__(self):
        self._items = []
    
    def add_item(self, name, price, category):
        item = Item(name, price, category)

        self._items.append(item)

    @property
    def items(self):
        return self._items