from Domain.rezervare import *
from Domain.rezervare2 import *


def add(lista_rezervari: list, _id: int, _nume: str, _clasa: str, _pret: int, _checkin: bool):
    reservation = get_new_reservation(_id, _nume, _clasa, _pret, _checkin)
    return lista_rezervari + [reservation]


def read(lista_rezervari: list, id_rezervare: int = None):
    rezervarea_gasita = None

    if id_rezervare is None:
        return lista_rezervari

    for reservation in lista_rezervari:
        if get_id(reservation) == id_rezervare:
            rezervarea_gasita = reservation

        return rezervarea_gasita


def update(lista_rezervari, new_reservation):
    result = []

    for reservation in lista_rezervari:
        if get_id(reservation) == get_id(new_reservation):
            result.append(new_reservation)
        else:
            result.append(reservation)

    return result


def delete(lista_rezervari, id_rezervare: int):
    result = []

    for reservation in lista_rezervari:
        if get_id(reservation) != id_rezervare:
            result.append(reservation)

    return result
