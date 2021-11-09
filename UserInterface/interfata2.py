from UserInterface.interfata import *
from Logic.reducere import *


def handle_show_all2(lista):
    """
    Functia afiseaza toate rezervarile cu toate detaliile acestora du=in lista de rezervari
    :param lista: lista rezervarilor
    """
    for reservation in lista:
        print(get_reservation_string(reservation))


def meniu():
    print("add,id (un numar),nume (un nume),clasa (economy / economy plus / business),pret (un numar),checkin (da/nu)")
    print("delete,id (un numar)")
    print("showall")
    print("high class,nume (numele pentru care doriti schimbarea clasei)")
    print("reducere,procentul (un numar)")
    print("iesire")
    print("ajutor")


def command(lista_noua):
    meniu()
    while True:
        optiune = input("Dati comenzile: ")
        if optiune == "ajutor":
            meniu()
        else:
            cuvinte = optiune.split(";")
            if cuvinte[0] == "iesire":
                break
            else:
                for rezervare in cuvinte:
                    cuvant = rezervare.split(",")
                    if cuvant[0] == "add":
                        try:
                            idul = int(cuvant[1])
                            nume = cuvant[2]
                            clasa = cuvant[3]
                            price = float(cuvant[4])
                            checkin = cuvant[5]
                            lista_noua = create(lista_noua, idul, nume, clasa, price, checkin)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                            return lista_noua
                    elif cuvant[0] == 'delete':
                        try:
                            idul = cuvant[1]
                            idul = int(idul)
                            lista_noua = delete(lista_noua, idul)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                            return lista_noua
                    elif cuvant[0] == 'showall':
                        handle_show_all2(lista_noua)
                    elif cuvant[0] == 'high class':
                        numele_cautat = cuvant[1]
                        lista_noua = get_higher_class(lista_noua, numele_cautat)
                    elif cuvant[0] == 'reducere':
                        procent = int(cuvant[1])
                        lista_noua = reduce_pret_pentru_chk(lista_noua, procent)
                    else:
                        print("Comanda gresita! Reincercati sau tastati 'ajutor' pentru a vedea comenzile")
