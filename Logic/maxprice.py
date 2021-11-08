from Domain.rezervare import *


def max_price_for_class(lista):
    """
    Functia va parcurge toate rezervarile si in functie de clasele rezervarilor, returna maximul pentru fiecare.
    :param lista: lista de rezervari
    :return: maximele pentru fiecare clasa
    """
    try:
        max_economy = 0
        max_economy_plus = 0
        max_business = 0
        for reservation in lista:
            if get_class(reservation) == 'economy':
                if max_economy < get_price(reservation):
                    max_economy = get_price(reservation)
            elif get_class(reservation) == 'economy plus':
                if max_economy_plus < get_price(reservation):
                    max_economy_plus = get_price(reservation)
            else:
                if max_business < get_price(reservation):
                    max_business = get_price(reservation)

        return max_economy, max_economy_plus, max_business
    except ValueError as ve:
        print('Eroare:', ve)
