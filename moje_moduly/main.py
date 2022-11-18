print("------------------------------")
print("--------MODUŁY----main.py-----------------")
print("------------------------------------\n")

# print("\n----importowanie modułu--------------------------")
# import dane
# print(dane.nb)
# print(dane.book)

print("\n----importowanie funkcji z modułu z innego katalogu--------------------------")
from moje_funkcje.bfunkcje import czytaj, czytaj_dict


print("\n----importowanie klasy z modułu (który zawiera funkcje) z innego katalogu--------------------------")
from moje_klasy.cdane import CDane


print("\n----importowanie modułu z aliasem--------------------------")
import dane as dn
print(dn.nb)
print(dn.book)

print("\n----importowanie modułu z funkcjami bezposrednio--------------------------")
from dane import nb, book
print(nb)
print(book)

# # jak działa enumerate:
# print(list(enumerate(nb)))
# print(list(enumerate(nb, 101)))

print("\n----importowanie modułu z biblioteki, z innego katalogu--------------------------")
czytaj_dict(book)
czytaj(book["n_filii"])

print("\n----importowanie klasy z modułu (który zawiera funkcje) z innego katalogu--------------------------")
cd = CDane(nb, book)
cd.czytaj_liste()
print("przerywnik")
cd.czytaj_slownik()
