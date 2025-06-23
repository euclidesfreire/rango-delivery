class Category:
    _id: int
    _name: str
    _food_establishment_id: int

    def __init__(self, id, name, food_establishment_id):
        self._name = name
        self._id = id
        self._food_establishment_id = food_establishment_id

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def food_establishment_id(self):
        return self._food_establishment_id