from entity.foodestablishment import FoodEstablishment

class FoodEstablishmentService:

    _foodestablishments: list

    def __init__(self):
        self._foodestablishments = []
     
    def add(self, name, category):

        if (not name.strip()) | (not category.strip()):
            return False

        foodestablishmentNew = {}

        foodestablishmentNew[name] = FoodEstablishment(name, category)

        self._foodestablishments.append(foodestablishmentNew)

        return foodestablishmentNew
    
    def read(self):
        for key in self._foodestablishments:
            print(key)
            #print(f'Name: {value._name} | Category: {value._category} | Status: {value._status}')

    @property
    def toggle_status(self, name):
        if name not in self._foodestablishments:
            return False
        
        #fes = _foodestablishments[name]

        #return self._status

