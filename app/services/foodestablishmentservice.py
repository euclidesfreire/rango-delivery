from entity.foodestablishment import FoodEstablishment

class FoodEstablishmentService:
    _food_establishments: list

    def __init__(self):
        self._food_establishments = {}
     
    def add(self, id, name, category):

        if (not id) | (not name.strip()) | (not category.strip()):
            return False

        food_establishment_new = FoodEstablishment(id, name, category)

        self._food_establishments[id] = food_establishment_new

        return food_establishment_new
    
    @property
    def read(self):
        #Columns name
        columns_name = f'\n{'Id'.ljust(10)} | {'Name'.ljust(25)} | {'Category'.ljust(25)} | {'Rating'.ljust(10)} | Status'
        print(columns_name)
        print('=' * len(columns_name))

        #Values
        for fe in self._food_establishments.values():
            print(f'{str(fe.id).ljust(10)} | {fe.name.ljust(25)} | {fe.category.ljust(25)} | {str(fe.mean_rating).ljust(10)} | {fe.status}')

    def toggle_status(self, id):
        if id not in self._food_establishments.keys():
            return False
        
        fes = self._food_establishments[id]

        fes.toggle_status

        return fes.status

    def add_rating(self, id, user_id, value):
        if id not in self._food_establishments.keys():
            return False
        
        if not (0 < value < 5):
            return False

        fes = self._food_establishments[id]

        fes.add_rating(user_id, value)

        return True
    
    def rating_of(self, id):
        if id not in self._food_establishments.keys():
            return False
        
        fes = self._food_establishments[id]

        return fes.rating
    
    def mean_rating(self, id):
        if id not in self._food_establishments.keys():
            return False
        
        fes = self._food_establishments[id]

        return fes.mean_rating