from Domain.rezervare import *


def reduce_pret_pentru_chk(lista, procent):

    if not (0 <= procent <= 100):
        raise ValueError("Procentajul dat trebuie sa fie intre 0 si 100")

    result = []
    for reservation in lista:
        if get_checkin(reservation):
            pret_nou = get_price(reservation) * (100 - procent) / 100
            result.append(get_new_reservation(
                get_id(reservation),
                get_name(reservation),
                get_class(reservation),
                pret_nou,
                get_checkin(reservation),
                ))
        else:
            result.append(reservation)

    return result
