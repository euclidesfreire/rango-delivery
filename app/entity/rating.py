class Rating:
    _user_id: int
    _value: float

    def __init__(self, user_id, value):
        self._user_id = user_id
        self._value = value

    @property
    def value(self):
        return self._value
    
    def value(self, value):
        self._value = value