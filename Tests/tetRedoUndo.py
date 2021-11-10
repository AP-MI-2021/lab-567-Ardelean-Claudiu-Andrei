from UserInterface.interfata import handle_undo, handle_redo, handle_new_list
from Logic.logic import *


def test_undo_redo():
    list_versions = [[]]
    current_version = 0
    lista = []
    lista = create(lista, 1, "Andrei", "economy plus", 180, "da")
    list_versions, current_version = handle_new_list(list_versions, current_version, lista)
    lista = create(lista, 2, "Carmen", "economy plus", 100, "nu")
    list_versions, current_version = handle_new_list(list_versions, current_version, lista)
    lista = create(lista, 3, "Andreea", "business", 249.9, "nu")
    list_versions, current_version = handle_new_list(list_versions, current_version, lista)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": 2, "nume": "Carmen", "clasa": "economy plus", "pret": 100, "checkin": "nu"},
                     {"id": 3, "nume": "Andreea", "clasa": "business", "pret": 249.9, "checkin": "nu"}]
    lista, current_version = handle_undo(list_versions, current_version)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": 2, "nume": "Carmen", "clasa": "economy plus", "pret": 100, "checkin": "nu"}]

    lista, current_version = handle_undo(list_versions, current_version)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"}]

    lista, current_version = handle_undo(list_versions, current_version)
    assert lista == []

    lista = create(lista, 1, "Andrei", "economy plus", 180, "da")
    list_versions, current_version = handle_new_list(list_versions, current_version, lista)
    lista = create(lista, 2, "Carmen", "economy plus", 100, "nu")
    list_versions, current_version = handle_new_list(list_versions, current_version, lista)
    lista = create(lista, 3, "Andreea", "business", 249.9, "nu")
    list_versions, current_version = handle_new_list(list_versions, current_version, lista)
    lista, current_version = handle_redo(list_versions, current_version)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": 2, "nume": "Carmen", "clasa": "economy plus", "pret": 100, "checkin": "nu"},
                     {"id": 3, "nume": "Andreea", "clasa": "business", "pret": 249.9, "checkin": "nu"}]

    lista, current_version = handle_undo(list_versions, current_version)
    lista, current_version = handle_undo(list_versions, current_version)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"}]

    lista, current_version = handle_redo(list_versions, current_version)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": 2, "nume": "Carmen", "clasa": "economy plus", "pret": 100, "checkin": "nu"}]

    lista, current_version = handle_redo(list_versions, current_version)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": 2, "nume": "Carmen", "clasa": "economy plus", "pret": 100, "checkin": "nu"},
                     {"id": 3, "nume": "Andreea", "clasa": "business", "pret": 249.9, "checkin": "nu"}]

    lista, current_version = handle_undo(list_versions, current_version)
    lista, current_version = handle_undo(list_versions, current_version)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"}]

    lista = create(lista, 4, "Mircea", "economy", 150, "da")
    list_versions, current_version = handle_new_list(list_versions, current_version, lista)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": 4, "nume": "Mircea", "clasa": "economy", "pret": 150, "checkin": "da"}]
    lista, current_version = handle_redo(list_versions, current_version)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": 4, "nume": "Mircea", "clasa": "economy", "pret": 150, "checkin": "da"}]

    lista, current_version = handle_undo(list_versions, current_version)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"}]

    lista, current_version = handle_undo(list_versions, current_version)
    assert lista == []

    lista, current_version = handle_redo(list_versions, current_version)
    lista, current_version = handle_redo(list_versions, current_version)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": 4, "nume": "Mircea", "clasa": "economy", "pret": 150, "checkin": "da"}]

    lista, current_version = handle_redo(list_versions, current_version)
    assert lista == [{"id": 1, "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": 4, "nume": "Mircea", "clasa": "economy", "pret": 150, "checkin": "da"}]
