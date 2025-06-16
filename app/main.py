from services.foodestablishmentservice import FoodEstablishmentService

fes = FoodEstablishmentService()

fes.add('Cebola', 'Brasileira')
fes.add('Império da Juçara', 'Juçara')
fes.add('Império das Ostras', 'Mar')

fes.read

fes.toggle_status('Cebola')

fes.read