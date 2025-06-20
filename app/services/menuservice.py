from entity.menu.menu import Menu

class MenuService:

    _menu: Menu

    def __init__(self):
        self._menu = Menu()

    def add_item(self, name, price, category):
        self._menu.add_item(name, price, category)
    
    def read(self):
        print(self._menu.items)