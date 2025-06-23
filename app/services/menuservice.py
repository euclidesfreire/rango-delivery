from entity.menu.category import Category
from entity.menu.product import Product

class MenuService:
    _categories: dict
    _products: dict

    def __init__(self):
        self._categories = {}
        self._products = {}

    def add_category(self, id, name, food_establishment_id):
        if id in self._categories.keys():
            return False
        
        self._categories[id] =  Category(id, name, food_establishment_id)

    def add_product(self, id, name, price, description, category_id):
        if category_id not in self._categories.keys():
            return False
        
        if id in self._products.keys():
            return False
       
        self._products[id] = Product(id, name, price, description, category_id)
    
    def read(self, food_establishment_id):
        if not self._categories:
            return None
        
        #Filter Categories by food_establishment_id        
        categories_select = [category.id for category in self._categories.values() if category.food_establishment_id == food_establishment_id]

        #Filter Produtcs by Categories Select
        products_select = [product for product in self._products.values() if product.category_id in categories_select]

        for category_id in categories_select:

            category = self._categories[category_id]

            print(f'\n{category.name}')
            print(f'{len(category.name)*'-'}\n')

            for product in products_select:

                if product.category_id == category_id:
                    print(f'{product.name.ljust(25)} | {str(product.price).ljust(8)}')
                    print(f'{product.description.ljust(15)}\n')