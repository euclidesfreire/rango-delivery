class FoodEstablishment:
    name: str
    category: str
    status: bool

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.status = False