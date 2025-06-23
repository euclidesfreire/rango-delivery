class Product:
    _id: int
    _name: str
    _price: float
    _description: str
    _category_id: int

    def __init__(self, id, name, price, description, category_id):
        '''
        Create product new
        
        Parameters
        ----------
        id: int
        name: str
        price: float
        description: str
        category: int
        '''
        self._id = id
        self._name = name
        self._price = price
        self._description = description
        self._category_id = category_id

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price

    @property
    def description(self):
        return self._description
    
    @property
    def category_id(self):
        return self._category_id