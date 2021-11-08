from Domain.rezervare import *
# from Domain.rezervare2 import *


def create(lista_rezervari: list, _id: int, _nume: str, _clasa: str, _pret: float, _checkin: str):
    """
    Functoa va creea o intrare noua in lista de rezervari
    :param lista_rezervari: lista de rezervari
    :param _id: id-ul rezeervarii
    :param _nume: numere pe care este facuta rezervarea
    :param _clasa: clasa la care este facuta rezervarea
    :param _pret: pretul rezervarii
    :param _checkin: checkinul rezervarii
    :return: o rezervare noua la lista de rezervari
    """
    reservation = get_new_reservation(_id, _nume, _clasa, _pret, _checkin)
    return lista_rezervari + [reservation]


def read(lista_rezervari: list, id_rezervare: int = None):
    """
    Functia ajuata la citirea datelor despre o rezervare.
    :param lista_rezervari: lista de rezervari
    :param id_rezervare: id-ul unei rezervari
    :return: detaliile rezervarii id-ului citit.
    """
    rezervarea_gasita = None

    if id_rezervare is None:
        return lista_rezervari

    for reservation in lista_rezervari:
        if get_id(reservation) == id_rezervare:
            rezervarea_gasita = reservation

        return rezervarea_gasita


def update(lista_rezervari, new_reservation):
    """
    Functia inlocuieste in lista actuala, detaliile rezervarii pentru care se citesc de catre utilizator.
    :param lista_rezervari: lista de rezervari
    :param new_reservation: dictionarul cu noile detalii.
    :return: lista cu modificarile efectuate
    """
    result = []

    for reservation in lista_rezervari:
        if get_id(reservation) == get_id(new_reservation):
            result.append(new_reservation)
        else:
            result.append(reservation)

    return result


def delete(lista_rezervari, id_rezervare: int):
    """
    Functia va sterge din lista rezervarea corespondenta id-ului citit.
    :param lista_rezervari: lista de rezervari
    :param id_rezervare: id-ul rezervarii pentru care se vor face modificarile
    :return: lista rezultata in urma modificarilor
    """
    result = []

    for reservation in lista_rezervari:
        if get_id(reservation) != id_rezervare:
            result.append(reservation)

    return result
