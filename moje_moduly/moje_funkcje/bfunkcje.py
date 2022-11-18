"""
tworzymy Bibliotekę

nowy modul Python - bfunkcje.py
w katalogu moje_funkcje

"""

def czytaj(lista):
    for i,j in enumerate(lista):
        print(f"element list nr {i+1} --> {j}")

def czytaj_dict(dict):
    for x, y in dict.items():
        print(f"klucz --> {x} : wartość --> {y}")
