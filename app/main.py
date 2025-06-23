from services.foodestablishmentservice import FoodEstablishmentService
from services.menuservice import MenuService

fes = FoodEstablishmentService()

fes.add(1, 'Cebola', 'Brasileira')
fes.add(2, 'Império da Juçara', 'Juçara')
fes.add(3, 'Império das Ostras', 'Mar')
fes.add(4, 'Diverno', 'Sorveteria')

fes.toggle_status(1)

fes.add_rating(1, 1,3.5)
fes.add_rating(1, 2,4.5)
fes.add_rating(1, 3,2)
fes.add_rating(2, 1,4)
fes.add_rating(3, 1,4.5)

#rating fora do padrão
fes.add_rating(1, 3,6)
fes.add_rating(3, 1,-2)


fes.read

#Menu
menu = MenuService()

#1 - Cebola 
menu.add_category(1, "Principal", 1)
menu.add_category(5, "Bebidas", 1)

#2 - Império da Juçara 
menu.add_category(2, "Juçara Menu", 2)

#3 - Império das Ostras
menu.add_category(3, "Mar Principal", 3)
menu.add_category(6, "Mar Bebidas", 3)

#4 - Diverno
menu.add_category(4, "Diverno Menu", 4)

#products
#1 - Cebola 
menu.add_product(1, 'Cebola Frita', 36.45, 'Famosa Cebola crocante', 1)
menu.add_product(2, 'Carne do Sol com Cebola', 75, 'Maravilhosa Carne de Sol da casa', 1)
menu.add_product(3, 'Suco de Cajú', 12, 'Suco dos sucos', 5)

menu.read(1)

#3 - Império das Ostras
menu.add_product(4, 'Ostras', 20, '12 ostras super frescas', 3)
menu.add_product(5, 'Balde de ostras', 45, '5 dúzia de ostras super frescas', 3)
menu.add_product(6, 'Suco de Cajá', 13, '', 6)
menu.add_product(7, 'Refrigerante Coca-cola', 13, '', 6)

menu.read(3)