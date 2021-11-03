from Domain.rezervare import *
# from Domain.rezervare2 import *
from Logic.logic import create, read, update, delete


def get_data():
    return [
        get_new_reservation(1, "r1", "economy", 100, True),
        get_new_reservation(2, "r2", "economy plus", 520, True),
        get_new_reservation(3, "r3", "business", 2200, True),
        get_new_reservation(4, "r4", "economy plus", 870, True),
        get_new_reservation(5, "r5", "economy", 90, True)
    ]


def test_read():
    lista = get_data()
#    reservation = lista[2]
#    assert read(lista, get_id(reservation)) == get_new_reservation(3, "r3", "business", 2200, True)
    assert read(lista, None) == lista


def test_update():
    lista = get_data()
    new_reservation = get_new_reservation(2, 'p6', 'desc 6', 40.32, True)
    lista_noua = update(lista, new_reservation)
    assert len(lista) == len(lista_noua)
    assert new_reservation in lista_noua
#    assert lista[2] != lista_noua[2]


def test_delete():
    lista = get_data()
    delete_id = 3
    deleted_reservation = read(lista, delete_id)
    lista_noua = delete(lista, delete_id)
    assert len(lista_noua) == len(lista) - 1
    assert deleted_reservation not in lista_noua


def test_create():
    lista = get_data()
    new_reservation = get_new_reservation(6, "r6", "economy", 40, True)
    lista_noua = create(lista, 6, "r6", "economy", 40, True)

    assert len(lista_noua) == len(lista) + 1
    assert new_reservation in lista_noua


def tests():
    test_create()
    test_update()
    test_delete()
    test_read()


tests()
