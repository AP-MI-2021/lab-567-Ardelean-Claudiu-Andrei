from Domain.rezervare import *
from Logic.logic import *
from UserInterface.interfata import *


def handle_show_all(lista):
    """
    Functia afiseaza toate rezervarile cu toate detaliile acestora du=in lista de rezervari
    :param lista: lista rezervarilor
    """
    for reservation in lista:
        print(get_reservation_string(reservation))


def meniu():
    print("add, id, nume, clasa, pret, checkin")
    print("delete, id")
    print("showall")
    print("iesire")


def command(lista_noua):
    while True:
        optiune = input("Dati comenzile: ")
        if optiune == "ajutor":
            meniu()
        else:
            cuvinte = optiune.split(";")
            if cuvinte[0] == "iesire":
                break
            else:
                print(cuvinte)
                for rezervare in cuvinte:
                    cuvant = rezervare.split(",")
                    if cuvant[0] == "add":
                        try:
                            idul = int(cuvant[1])
                            nume = cuvant[2]
                            clasa = cuvant[3]
                            price = float(cuvant[4])
                            checkin = cuvant[5]
                            lista_noua = get_new_reservation(idul, nume, clasa, price, checkin)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                            return lista_noua
                    elif cuvant[0] == 'delete':
                        try:
                            idul = cuvant[1]
                            lista_noua = delete(idul, lista_noua)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                            return lista_noua
                    elif cuvant[0] == 'showall':
                        handle_show_all(lista_noua)
                    else:
                        print("Comanda gresita! Reincercati sau tastati 'ajutor' pentru a vedea comenzile")
