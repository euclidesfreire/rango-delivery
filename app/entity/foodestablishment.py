class FoodEstablishment:
    _name: str
    _category: str
    _status: bool

    def __init__(self, name, category):
        self._name = name  
        self._category = category
        self._status = False
    
    @property
    def status(self):
        return '✅' if self._status else '🟥' 
    
    @property
    def toggle_status(self):
        self._status = not self._status

        return self._status

    @property
    def name(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def category(self, category):
        self._category = category

    @property
    def category(self):
        return self._category