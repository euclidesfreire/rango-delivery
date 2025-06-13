class FoodEstablishment:
    _name: str
    _category: str
    _status: bool

    def __init__(self, name, category):
        self._name = name  
        self._category = category
        self._status = False
    
    @property
    def toggle_status(self):
        self._status = not self._status

        return self._status