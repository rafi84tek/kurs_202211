"""
cdane.py

"""
print("\n----importowanie funkcji z bfunkcje.py--------------------------")
from moje_funkcje.bfunkcje import *

class CDane:
    def __init__(self, lista, dict):
        self.dict = dict
        self.lista = lista

    def czytaj_liste(self):
        return czytaj(self.lista)

    def czytaj_slownik(self):
        return czytaj_dict(self.dict)

