from Domain.rezervare import *
from Domain.rezervare2 import *
from Logic.logic import *


def get_data():
    return [
        get_new_reservation(1, "r1", "economy", 100, True),
        get_new_reservation(2, "r2", "economy plus", 520, True),
        get_new_reservation(3, "r3", "business", 2200, True),
        get_new_reservation(4, "r4", "economy plus", 870, True),
        get_new_reservation(5, "r5", "economy", 90, True)
    ]


def test_add():
    lista = get_data()
    new_reservation = get_new_reservation(6, "r6", "economy", 40, True)
    lista_noua = add(lista, new_reservation)

    assert len(lista_noua) == len(lista) + 1
    assert new_reservation in lista_noua


def tests():
    test_add()


tests()
