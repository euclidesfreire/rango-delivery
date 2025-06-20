from entity.menu.product import Product

class Category:
    _name: str
    _product: list

    def __init__(self, name):
        self._name = name
        self._product = []

    def add_product(self, name, price, description):
        product_new = Product(name, price, description)

        self._product.append(product_new)
    
    @property
    def product(self):
        return self._product