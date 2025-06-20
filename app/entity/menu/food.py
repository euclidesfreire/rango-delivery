from entity.menu.item from Item

class Food(Item):
    _descricao: str

    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._category = category