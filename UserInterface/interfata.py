
from Logic.logic import *
from Logic.reducere import reduce_pret_pentru_chk


def handle_add(lista):
    try:
        id_rezervare = int(input('Dati id-ul rezervarii: '))
        nume = input('Dati numele pe care s-a facut rezervarea: ')
        clasa = input('Dati clasa la care s-a facut rezervarea (economy / economy plus / business): ')
        while clasa != "economy" and clasa != "economy plus" and clasa != "business":
            clasa = input('Dati clasa la care s-a facut rezervarea (economy / economy plus / business): ')
        pret = float(input('Dati pretul rezervarii: '))
        checkin = input('Dati valoarea checkin-ului rezervarii (True / False): ')
        while checkin != "True" and checkin != "true" and checkin != "False" and checkin != "false":
            checkin = (input('Dati valoarea checkin-ului rezervarii (True / False): '))
        if checkin == 'False' or checkin == 'false':
            checkin = False
        else:
            checkin = bool(checkin)
        return create(lista, id_rezervare, nume, clasa, pret, checkin)
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


def handle_show_all(lista):
    for reservation in lista:
        print(get_reservation_string(reservation))


def handle_show_details(lista):
    try:
        id_reservation = int(input('Dati id-ul rezervarii pentru care doriti detalii: '))
        reservation = read(lista, id_reservation)
        print(f'Nume: {get_name(reservation)}')
        print(f'Clasa: {get_class(reservation)}')
        print(f'Pret: {get_price(reservation)}')
        print(f'Checkin: {get_checkin(reservation)}')
    except ValueError as ve:
        print('Eroare:', ve)


def handle_update(lista):
    try:
        id_reservation = int(input('Dati id-ul rezervarii care se actualizeaza: '))
        nume = input('Dati noul nume al rezervarii: ')
        clasa = input('Dati noua clasa a rezervarii: ')
        while clasa != "economy" and clasa != "economy plus" and clasa != "business":
            clasa = input('Dati clasa la care s-a facut rezervarea (economy / economy plus / business): ')
        pret = float(input('Dati noul pret al rezervarii: '))
        checkin = input('Dati valoarea checkin-ului rezervarii (True / False): ')
        while checkin != "True" and checkin != "true" and checkin != "False" and checkin != "false":
            checkin = (input('Dati valoarea checkin-ului rezervarii (True / False): '))
        if checkin == 'False' or checkin == 'false':
            checkin = False
        else:
            checkin = bool(checkin)
        return update(lista, get_new_reservation(id_reservation, nume, clasa, pret, checkin))
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


def handle_delete(lista):
    try:
        id_reservation = int(input('Dati id-ul rezervarii care se va sterge: '))
        lista = delete(lista, id_reservation)
        print('Stergerea a fost efectuata cu succes.')
        return lista
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


def get_higher_class(lista, name):
    result = []
    for x in lista:
        if get_name(x) == name:
            if get_class(x) == "economy":
                new_class = "economy plus"
                reservation = get_new_reservation(
                    get_id(x),
                    get_name(x),
                    new_class,
                    get_price(x),
                    get_checkin(x)
                )
                result.append(reservation)

            elif get_class(x) == "economy plus":
                new_class = "business"
                reservation = get_new_reservation(
                    get_id(x),
                    get_name(x),
                    new_class,
                    get_price(x),
                    get_checkin(x)
                )
                result.append(reservation)
            elif get_class(x) == "business":
                new_class = "business"
                reservation = get_new_reservation(
                    get_id(x),
                    get_name(x),
                    new_class,
                    get_price(x),
                    get_checkin(x)
                )
                result.append(reservation)
            else:
                result.append(x)
    return result


def handle_upper_class(lista):
    try:
        numele_cautat = input('Introduceti numele pentru care doriti sa scimbati clasa: ')
        lista = get_higher_class(lista, numele_cautat)
        print("Clasa rezervarilor a fost modificata cu success")
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


def handle_crud(lista):
    print('1. Adaugare')
    print('2. Modificare')
    print('3. Stergere')
    print('a. Afisare')
    print('d. Detalii rezervare')
    # print('b. Revenire')

    optiune = input('Optiunea aleasa: ')
    if optiune == '1':
        lista = handle_add(lista)
    elif optiune == '2':
        lista = handle_update(lista)
    elif optiune == '3':
        lista = handle_delete(lista)
    elif optiune == 'a':
        handle_show_all(lista)
    elif optiune == 'd':
        handle_show_details(lista)
    else:
        print('Optiune invalida.')
    return lista


def handle_reducere(lista):
    try:

        procentaj_reducere = int(input("Dati un procentaj de reducere(0-100):"))

        lista = reduce_pret_pentru_chk(lista, procentaj_reducere)

        print("Pretul rezervarilor a fost redus cu success")
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


# def handle_ordonare(prajituri):
#    try:
#        prajituri = ordonare_prajituri(prajituri)
#    except ValueError as ve:
#        print('Eroare:', ve)
#
#    return prajituri


def show_menu():
    print('1. CRUD')
    print('2. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.')
    print('3. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.')
    '''print('7. Undo')'''
    print('x. Exit')


def handle_new_list(list_versions, current_version, lista):
    while current_version < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(lista)
    current_version += 1
    return list_versions, current_version


def handle_undo(list_versions, current_version):
    if current_version < 1:
        print("Nu se mai poate face undo.")
        return
    current_version -= 1
    return list_versions[current_version], current_version


def handle_redo(list_versions, current_version):
    if current_version == len(list_versions) - 1:
        print("Nu se mai poate face redo.")
        return
    current_version += 1
    return list_versions[current_version], current_version


def run_ui(lista):

    list_versions = [lista]
    current_version = 0

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            lista = handle_crud(lista)
            list_versions, current_version = handle_new_list(list_versions, current_version, lista)
        elif optiune == '2':
            lista = handle_upper_class(lista)
            list_versions, current_version = handle_new_list(list_versions, current_version, lista)
        elif optiune == '3':
            lista = handle_reducere(lista)
            list_versions, current_version = handle_new_list(list_versions, current_version, lista)
        elif optiune == '7':
            list_versions, current_version = handle_undo(list_versions, current_version)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return lista
