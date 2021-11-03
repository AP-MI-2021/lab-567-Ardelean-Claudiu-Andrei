from UserInterface.interfata import *
from Tests.tests import *


def main():
    lista = []
    lista = create(lista, 1, 'Ardelean', 'business', 1000, True)
    lista = create(lista, 2, 'Borbei', 'business', 1050, False)
    lista = create(lista, 3, 'Reitler', 'economy', 125.50, False)
    lista = create(lista, 4, 'turoczi', 'economy plus', 500, True)
    lista = create(lista, 5, 'Gozner', 'business :', 1462.30, True)
    lista = create(lista, 6, 'Capusan', 'economy', 40.5, False)
    lista = create(lista, 7, 'Musk', 'economy', 34.99, False)
    run_ui(lista)


if __name__ == '__main__':
    tests()
    main()
