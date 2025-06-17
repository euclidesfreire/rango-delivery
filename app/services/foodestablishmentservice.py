from entity.foodestablishment import FoodEstablishment

class FoodEstablishmentService:

    _food_establishments: list

    def __init__(self):
        self._food_establishments = {}
     
    def add(self, name, category):

        if (not name.strip()) | (not category.strip()):
            return False

        food_establishment_new = FoodEstablishment(name, category)

        self._food_establishments[name] = food_establishment_new

        return food_establishment_new
    
    @property
    def read(self):
        #Columns name
        columns_name = f'\n{'Name'.ljust(25)} | {'Category'.ljust(25)} | Status'
        print(columns_name)
        print('=' * len(columns_name))

        #Values
        for fe in self._food_establishments.values():
            print(f'{fe.name.ljust(25)} | {fe.category.ljust(25)} | {fe.status}')

    def toggle_status(self, name):
        if name not in self._food_establishments.keys():
            return False
        
        fes = self._food_establishments[name]

        fes.toggle_status

        return fes.status

    def add_rating(self, name, user_id, value):
        if name not in self._food_establishments.keys():
            return False
        
        fes = self._food_establishments[name]

        fes.add_rating(user_id, value)

        return True
    
    def rating_of(self, name):
        if name not in self._food_establishments.keys():
            return False
        
        fes = self._food_establishments[name]

        return fes.rating
    
    def mean_rating(self, name):
        if name not in self._food_establishments.keys():
            return False
        
        fes = self._food_establishments[name]

        return fes.mean_rating