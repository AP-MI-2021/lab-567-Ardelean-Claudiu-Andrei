from Domain.rezervare import *


def sum_for_name(lista):
    """
    Functia returneaza suma preturilor penru fiecare Nume
    :param lista: lista cu rezervari
    :return: o lista cu suma preturilor pentru fiecare nume
    """
    try:
        result = {}
        for reservation in lista:
            nume = get_name(reservation)
            price = get_price(reservation)
            if nume in result:
                result[nume] = result[nume] + price
            else:
                result[nume] = price
        return result
    except ValueError as ve:
        print('Eroare:', ve)
