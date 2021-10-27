def get_new_reservation(_id: int, _nume: str, _clasa: str, _pret: int, _checkin: bool):
    return [_id, _nume, _clasa, _pret, _checkin]


def get_id(reservation):
    return reservation[0]


def get_name(reservation):
    return reservation[1]


def get_class(reservation):
    return reservation[2]


def get_price(reservation):
    return reservation[3]


def get_checkin(reservation):
    return reservation[4]
