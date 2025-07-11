from entity.rating import Rating

class FoodEstablishment:
    _id: int
    _name: str
    _category: str
    _status: bool
    _rating: list

    def __init__(self, id, name, category):
        self._id = id  
        self._name = name  
        self._category = category
        self._status = False
        self._rating = {}
    
    @property
    def status(self):
        return '✅' if self._status else '🟥' 
    
    @property
    def toggle_status(self):
        self._status = not self._status

        return self._status
    @property
    def id(self):
        return self._id

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
    
    @property
    def rating(self):
        return self._rating
    
    def add_rating(self, user_id, value):
        rating_new = Rating(user_id, value)

        self._rating[user_id] = rating_new

    def search_rating(self, user_id):
        if user_id not in self._rating.keys():
            return False

        return self._rating[user_id]
    
    @property
    def mean_rating(self):
        if not self._rating:
            return 'N/A'

        sum_rating = sum(rating._value for rating in self._rating.values())

        mean = round(sum_rating / len(self._rating),1)

        return mean