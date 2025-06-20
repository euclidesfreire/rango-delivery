from entity.menu.item import Item

class Drink(Item):
    _name: str
    _price: float
    _descricao: str
    _category: str

    def __init__(self, name, price, category):
        self._name = name
        self._price = price
        self._category = category