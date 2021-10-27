from Domain.rezervare import *

from Domain.rezervare2 import *

from Logic.logic import add, read, update, delete

lista = []
lista = add(lista, 1, "Ardelean", "economy", 200, True)
lista = add(lista, 2, "Popescu", "business", 5000, False)


new_reservation = get_new_reservation(1, "Ionescu", "business", 2500, True)
lista = update(lista, new_reservation)

lista = delete(lista, 1)
rezervare = read(lista, 1)
print(rezervare)
rezervare = read(lista, 2)
print(rezervare)
