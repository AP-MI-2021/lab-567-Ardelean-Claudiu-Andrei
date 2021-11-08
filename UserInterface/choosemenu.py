from Logic.logic import create
from UserInterface.interfata import run_ui
from UserInterface.interfata2 import *


def alegeti_meniul():
    """
    Cu ajutorul functiei vom afisa meniul de meniuri
    """
    while True:
        print('1. Meniul 1.')
        print('2. Meniul 2. (SOON)')
        print('x. Exit.')
        lista = []
        lista = create(lista, 1, 'Ardelean', 'business', 1000, 'da')
        lista = create(lista, 2, 'Borbei', 'business', 1050, 'nu')
        lista = create(lista, 3, 'Reitler', 'economy', 125.50, 'nu')
        lista = create(lista, 4, 'Turoczi', 'economy plus', 500, 'da')
        lista = create(lista, 5, 'Gozner', 'business', 1462.30, 'da')
        lista = create(lista, 6, 'Capusan', 'economy', 40.5, 'nu')
        lista = create(lista, 7, 'Musk', 'economy', 34.99, 'nu')
        lista = create(lista, 8, 'Ardelean', 'economy', 250, 'da')
        optiune = input('alegeti optiunea: ')

        if optiune == '1':
            run_ui(lista)

        elif optiune == '2':
            command(lista)

        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')
