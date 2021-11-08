def get_new_reservation(_id: int, _nume: str, _clasa: str, _pret: float, _checkin: str):
    """
    Dictionarul in care se retin datele unei rezervari
    :param _id: id ul rezervarii, un nr intreg
    :param _nume: numeele pe care este facuta rezervarea
    :param _clasa: clasa de zbor
    :param _pret: pretul rezervarii
    :param _checkin: checkinul ("da" / "nu")
    :return: o rezervare
    """
    reservation = {
        'id': _id,
        'nume': _nume,
        'clasa': _clasa,
        'pret': _pret,
        'checkin': _checkin,
    }
    return reservation


def get_id(reservation):
    return reservation["id"]


def get_name(reservation):
    return reservation["nume"]


def get_class(reservation):
    return reservation["clasa"]


def get_price(reservation):
    return reservation["pret"]


def get_checkin(reservation):
    return reservation["checkin"]


def get_reservation_string(reservation):
    return f"{reservation['id']}, {reservation['nume']}, {reservation['clasa']}, {reservation['pret']},\
{reservation['checkin']}"
