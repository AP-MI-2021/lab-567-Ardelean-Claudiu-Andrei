# from Domain.rezervare2 import *
from Logic.logic import create, read, update, delete
from Logic.sum_for_name import *
from Logic.maxprice import *
from Logic.ordonare import *
from Logic.reducere import *
from UserInterface.interfata import get_higher_class
from Tests.tetRedoUndo import *

def get_data():
    return [
        get_new_reservation(1, "r1", "economy", 100, 'da'),
        get_new_reservation(2, "r2", "economy plus", 520, 'da'),
        get_new_reservation(3, "r3", "business", 2200, 'da'),
        get_new_reservation(4, "r4", "economy plus", 870, 'da'),
        get_new_reservation(5, "r5", "economy", 90, 'da')
    ]


def test_read():
    lista = get_data()
#    reservation = lista[2]
#    assert read(lista, get_id(reservation)) == get_new_reservation(3, "r3", "business", 2200, True)
    assert read(lista, None) == lista


def test_update():
    lista = get_data()
    new_reservation = get_new_reservation(2, 'p6', 'desc 6', 40.32, 'da')
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
    new_reservation = get_new_reservation(6, "r6", "economy", 40, 'da')
    lista_noua = create(lista, 6, "r6", "economy", 40, 'da')

    assert len(lista_noua) == len(lista) + 1
    assert new_reservation in lista_noua


def test_sum_for_name():
    lista = get_data()
    rezultat = sum_for_name(lista)

    assert len(rezultat) == 5
    assert rezultat["r1"] == 100
    assert rezultat["r2"] == 520
    assert rezultat["r3"] == 2200
    assert rezultat["r4"] == 870
    assert rezultat["r5"] == 90


def test_ordonare_rezervari():
    lista = []
    lista = create(lista, 1, "Robi", "economy", 100, "da")
    lista = create(lista, 2, "Andrei", "economy plus", 180, "nu")
    lista = create(lista, 3, "Gicu", "economy", 110, "nu")

    rezultat = ordonare_rezervari(lista)

    assert get_id(rezultat[0]) == 2
    assert get_id(rezultat[1]) == 3
    assert get_id(rezultat[2]) == 1


def test_max_price_for_class():
    lista = []
    lista = create(lista, 1, "Robi", "economy", 100, "da")
    lista = create(lista, 2, "Andrei", "economy plus", 180, "nu")
    lista = create(lista, 3, "Gicu", "economy", 110, "nu")
    lista = create(lista, 4, "Adi", "business", 1100, "nu")

    max_e, max_e_p, max_b = max_price_for_class(lista)

    assert max_e == 110
    assert max_e_p == 180
    assert max_b == 1100


def test_reduce_pret_pentru_chk():
    lista = []
    lista = create(lista, 1, "Robi", "economy", 100, "da")
    lista = create(lista, 2, "Andrei", "economy plus", 180, "nu")
    lista = create(lista, 3, "Gicu", "economy", 110, "nu")
    lista = create(lista, 4, "Adi", "business", 1100, "da")

    lista = reduce_pret_pentru_chk(lista, 50)
    assert get_price(lista[0]) == 50
    assert get_price(lista[3]) == 550


def test_get_higher_class():
    lista = []
    lista = create(lista, 1, "Robi", "economy", 100, "da")
    lista = create(lista, 2, "Andrei", "economy plus", 180, "nu")
    lista = create(lista, 3, "Gicu", "economy", 110, "nu")
    lista = create(lista, 4, "Adi", "business", 1100, "da")
    lista = create(lista, 5, "Andrei", "economy", 50, "da")

    lista = get_higher_class(lista, "Andrei")

    assert get_class(lista[1]) == "business"
    assert get_class(lista[4]) == "economy plus"


def tests():
    test_create()
    test_update()
    test_delete()
    test_read()
    test_sum_for_name()
    test_max_price_for_class()
    test_ordonare_rezervari()
    test_reduce_pret_pentru_chk()
    test_get_higher_class()
    test_undo_redo()


tests()
