from Logic.logic import *
from Logic.reducere import reduce_pret_pentru_chk
from Logic.maxprice import *
from Logic.ordonare import *
from Logic.sum_for_name import *


def handle_show_all(lista):
    """
    Functia afiseaza toate rezervarile cu toate detaliile acestora du=in lista de rezervari
    :param lista: lista rezervarilor
    """
    try:
        for reservation in lista:
            print(get_reservation_string(reservation))
    except ValueError as ve:
        print('Eroare:', ve)


def handle_show_details(lista):
    """
    Functia are rolul de a afisa detaliile unei rezervari pe bazaId-ului citit de la tastatura.
    :param lista: lista rezervarilor
    """
    try:
        id_reservation = int(input('Dati id-ul rezervarii pentru care doriti detalii: '))
        reservation = read(lista, id_reservation)
        print(f'Nume: {get_name(reservation)}')
        print(f'Clasa: {get_class(reservation)}')
        print(f'Pret: {get_price(reservation)}')
        print(f'Checkin: {get_checkin(reservation)}')
    except ValueError as ve:
        print('Eroare:', ve)


def handle_add(lista):
    """
    Functia are rolul de a citi datele necesare unei intrari noiin lista iar cu ajutorul functiei de create,
    construieste o intrare noua in lista de rezervari
    :param lista: lista rezervarilor
    :return: lista cu noua intare adaugata
    """
    try:
        id_rezervare = int(input('Dati id-ul rezervarii: '))
        nume = input('Dati numele pe care s-a facut rezervarea: ')
        clasa = input('Dati clasa la care s-a facut rezervarea (economy / economy plus / business): ')
        while clasa != "economy" and clasa != "economy plus" and clasa != "business":
            clasa = input('Dati clasa la care s-a facut rezervarea (economy / economy plus / business): ')
        price = float(input('Dati pretul rezervarii: '))
        checkin = input('Dati valoarea checkin-ului rezervarii (da / nu): ')
        while checkin != "Da" and checkin != "da" and checkin != "Nu" and checkin != "nu":
            checkin = (input('Dati valoarea checkin-ului rezervarii (da / nu): '))
        return create(lista, id_rezervare, nume, clasa, price, checkin)
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


def handle_update(lista):
    """
    Functia permite utilizatorului sa reintoduca datele unei rezervari pentru a le modifica prin recitirea acestora.
    :param lista: lista rezervarilor
    :return: lista rezervarilor modificata in urma parcurgerii procedurii de update
    """
    try:
        id_reservation = int(input('Dati id-ul rezervarii care se actualizeaza: '))
        nume = input('Dati noul nume al rezervarii: ')
        clasa = input('Dati noua clasa a rezervarii: ')
        while clasa != "economy" and clasa != "economy plus" and clasa != "business":
            clasa = input('Dati clasa la care s-a facut rezervarea (economy / economy plus / business): ')
        price = float(input('Dati noul pret al rezervarii: '))
        checkin = input('Dati valoarea checkin-ului rezervarii (da / nu): ')
        while checkin != "Da" and checkin != "da" and checkin != "Nu" and checkin != "nu":
            checkin = (input('Dati valoarea checkin-ului rezervarii (da / nu): '))
        return update(lista, get_new_reservation(id_reservation, nume, clasa, price, checkin))
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


def handle_delete(lista):
    """
    Functia citeste id-ul pentru care se doreste stergerea rezervarii si cu ajutorul functiei de delete, o sterge
     din lista.
    :param lista: lista rezervarilor
    :return: lista in urma modificariilor executate de functie
    """
    try:
        id_reservation = int(input('Dati id-ul rezervarii care se va sterge: '))
        lista = delete(lista, id_reservation)
        print('Stergerea a fost efectuata cu succes.')
        return lista
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


def get_higher_class(lista, name):
    """
    Functia parcurge lista si verifica pentru numele dorit de utilizator daca sa poate face modificare, iar daca
    este posibila o executa.
    :param lista: lista rezervarilor
    :param name: numele pentru care se doreste modificare clasei de zbor
    :return: lista rezervarilor cu clasa modificata penru numele primit
    """
    try:
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
    except ValueError as ve:
        print('Eroare:', ve)


def handle_upper_class(lista):
    """
    Functia se foloseste de variabila numele_cautat pentru a cauta si a modifica clasa rezervarii, cu ajutorul altei
    functii
    :param lista: lista rezervarilor
    :return: lista rezervarilor cu clasa modificata pentru numele la care s-a dorit aceasta actiune
    """
    try:
        numele_cautat = input('Introduceti numele pentru care doriti sa scimbati clasa: ')
        lista = get_higher_class(lista, numele_cautat)
        print("Clasa rezervarilor a fost modificata cu success")
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


def handle_crud(lista):
    """
    Aceasta funcrie afiseaza comenzile pentru functionaliatile CRUD-ului, iar la selectare se vor executa functiile.
    :param lista: lista rezervarilor
    :return: lista rezervarilor in uram executarii comenzilor
    """
    print('1. Adaugare')
    print('2. Modificare')
    print('3. Stergere')

    optiune = input('Optiunea aleasa: ')
    if optiune == '1':
        lista = handle_add(lista)
    elif optiune == '2':
        lista = handle_update(lista)
    elif optiune == '3':
        lista = handle_delete(lista)
    else:
        print('Optiune invalida.')
    return lista


def handle_reducere(lista):
    """
    Functia se foloseste de o functtie ajutatoare care verifica si aplica o reducere egala cu procentajul citit
    fiecarei rezervari a carei checkin este "da"
    :param lista: lista rezervarilor
    :return: lista rezervarilor cu preturile actualizate dupa reducere
    """
    try:

        procentaj_reducere = int(input("Dati un procentaj de reducere(0-100):"))

        lista = reduce_pret_pentru_chk(lista, procentaj_reducere)

        print("Pretul rezervarilor a fost redus cu success")
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


def handle_max_price(lista):
    """
    Functia afiseaza pretul maxim pentru fiecare clasa, cu ajutorul unei functii care verifica separat preturile si
    returneaza maximele pentru clase
    :param lista: lista rezervarilor
    """
    max_economy, max_economy_plus, max_business = max_price_for_class(lista)
    print(f'Pretul maxim pentru clasa Economy este {max_economy} unitati')
    print(f'Pretul maxim pentru clasa Economy Plus este {max_economy_plus} unitati')
    print(f'Pretul maxim pentru clasa Business este {max_business} unitati')


def handle_ordonare(lista):
    """
    Functia va returna o lista ordonata folosindu-se de o functie de ordonare.
    :param lista: lista rezervarilor
    :return: lista rezultata in urma ordonarii
    """
    try:
        lista = ordonare_rezervari(lista)
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


def handle_sum_for_name(lista):
    """
    Functia are rolul de a afisa pentru fiecare nume numa de pani pe care o are de platit persoana respectiva,
    folosindu-se de o functie separata care va calcula si va introduce in alta lista suma corescondenta numelui.
    :param lista: lista rezervarilor
    nu returneaza nimic, dar afiseaza suma pentru fiecare nume
    """
    try:
        result = sum_for_name(lista)
        for name in result:
            print(f'Numele {name} are suma preturilor {result[name]}')
    except ValueError as ve:
        print('Eroare:', ve)


def handle_new_list(list_versions, current_version, lista):
    """
    Functia are rolul de a inlocui in list_versions noua versiune a listei cu care lucram.
    :param list_versions: vesriunea listei care urmeaza sa fie actualizata
    :param current_version: numarul care reprezinta versiunea listei
    :param lista: noua lista dupa operatiune
    :return: lista actualizata care se va folosi mai departe
    """
    while current_version < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(lista)
    current_version += 1
    return list_versions, current_version


def handle_undo(list_versions, current_version):
    """
    Functia are rolul de a reface ulima modificare facuta listei inainte de ultima executare,
    respectiv o refacere a listei dupa executarea unui functionalitati.
    :param list_versions: vesriunea actuala a listei
    :param current_version: numarul care reprezinta versiunea listei
    :return: lista actualizata in urma executarii functiei
    """
    try:
        if current_version < 1:
            print("Nu se mai poate face undo.")
            return
        current_version -= 1
        return list_versions[current_version], current_version
    except ValueError as ve:
        print('Eroare:', ve)


def handle_redo(list_versions, current_version):
    """
    Functia are rolul de a reface ulima modificare facuta listei inainte de ultima executare,
    respectiv o refacere a listei dupa executarea unui Undo.
    :param list_versions: vesriunea actuala a listei
    :param current_version: numarul care reprezinta versiunea listei
    :return: lista actualizata in urma executarii functiei
    """
    try:
        if current_version == len(list_versions) - 1:
            print("Nu se mai poate face redo.")
            return
        current_version += 1
        return list_versions[current_version], current_version
    except ValueError as ve:
        print('Eroare:', ve)


def show_menu():
    """
    Functia show_menu are doar rol de printare si afiseaza optiunile meniului
    """
    print('1. Adaugare / Modificare / Stergere')
    print('2. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.')
    print('3. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.')
    print('4. Determinarea prețului maxim pentru fiecare clasă. ')
    print('5. Ordonarea rezervărilor descrescător după preț. ')
    print('6. Afișarea sumelor prețurilor pentru fiecare nume. ')
    print('7. Undo')
    print('8. Redo')
    print('a. Afisare')
    print('d. Detalii rezervare')
    print('x. Exit')


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
        elif optiune == '4':
            handle_max_price(lista)
        elif optiune == '5':
            lista = handle_ordonare(lista)
            list_versions, current_version = handle_new_list(list_versions, current_version, lista)
        elif optiune == '6':
            handle_sum_for_name(lista)
        elif optiune == '7':
            lista, current_version = handle_undo(list_versions, current_version)
        elif optiune == '8':
            lista, current_version = handle_redo(list_versions, current_version)
        elif optiune == 'a':
            handle_show_all(lista)
        elif optiune == 'd':
            handle_show_details(lista)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return lista
