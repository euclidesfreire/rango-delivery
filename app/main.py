from services.foodestablishmentservice import FoodEstablishmentService

fes = FoodEstablishmentService()

fes.add('Cebola', 'Brasileira')
fes.add('Império da Juçara', 'Juçara')
fes.add('Império das Ostras', 'Mar')

fes.read

fes.toggle_status('Cebola')

fes.read

fes.add_rating('Cebola', 1,3.5)
fes.add_rating('Cebola', 2,4.5)
fes.add_rating('Cebola', 3,2)
fes.add_rating('Império da Juçara', 1,4)
fes.add_rating('Império das Ostras', 1,4.5)

print("Mean Cebola")
print(fes.mean_rating('Cebola'))