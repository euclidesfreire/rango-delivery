class Product:
    _name: str
    _price: float
    _description: str

    def __init__(self, name, price, description):
        self._name = name
        self._price = price
        self._description = description