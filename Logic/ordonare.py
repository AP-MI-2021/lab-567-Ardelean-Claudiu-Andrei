from Domain.rezervare import *


def pret(reservation):
    """
    Functia reprezinta criteriul de ordonare al listei
    :param reservation: rezervarea
    :return: pretul rezervarii
    """
    return get_price(reservation)


def ordonare_rezervari(lista):
    """
    Functia returneaza lista ordonata dupa criteriile precizate.
    :param lista: lista de rezervari
    :return: lista ordonata
    """
    return sorted(lista, key=pret, reverse=True)
