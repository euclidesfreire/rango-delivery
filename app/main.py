from services.foodestablishmentservice import FoodEstablishmentService

fes = FoodEstablishmentService()

fes.add('Cebola', 'Brasileira')
fes.add('Império da Juçara', 'Juçara')
fes.add('Império das Ostras', 'Mar')
fes.add('Diverno', 'Sorveteria')

fes.toggle_status('Cebola')

fes.add_rating('Cebola', 1,3.5)
fes.add_rating('Cebola', 2,4.5)
fes.add_rating('Cebola', 3,2)
fes.add_rating('Império da Juçara', 1,4)
fes.add_rating('Império das Ostras', 1,4.5)

#rating fora do padrão
fes.add_rating('Cebola', 3,6)
fes.add_rating('Império das Ostras', 1,-2)


fes.read