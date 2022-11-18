print("witaj")
a = 6
print(a)
print(type(a))

a = "jeden"
print(a)
print(type(a))

# obiektowość Pythona powoduje, że zmienne mają zarezewowany kawałek pamięci i można zmieniać TYP

g: float  # ustalenie typu zmiennej, ale nie jest NA ZAWSZE
g = 2.234
print(g)
print(type(g))

g = True  # tu widać, że powyższe typowanie statyczne nie jest STAŁE
print(g)
print(type(g))

s = "lajkonik" #zmienna potraktowana jak LISTA, KOLEKCJA
print(s)
print(s[0])
print(s[1])
print(s[3:6]) #SLICE
print(s[-3])
#print(s[30])
print(s[30:])
print(s[::-1]) #liteorwanie od końca
sk = s[::-1]

print(s, sk)
print(s, sk, sep="--")
print(s + " " + sk)
print(f"{s} ----> {sk}")

d = 6.3453245
print(f"Wartosc d ={d:.2f}") #operatory na stringu, dzięki zastosowaniu f - formated string




kolory = ["czerwony", "czarny", "biały", "zielony", "niebieski"]
#stworzyc 2 listy: PARZ i NPARZ
print(kolory)

parz = kolory[::2] #od:do:STEP
nparz = kolory[1::2]
print(parz)
print(nparz)

#LISTY
""" nie ma limitu pamięci, ustalonej dlugosci"""
print(kolory[1])
print(kolory[1][1]) #wykazanie, ze tekst jest tez LISTĄ - zagniezdzenie

#print(kolory.sort()) #nie PRINTUJE, bo funkcja sort() nie daje wyniku, zwraca NONE
print(sorted(kolory)) #wykorzystanie funkcji SORTED
print(kolory)
kolory.sort() #sortowanie w miejscu, nieodwracalne
print(kolory)

#kopiowanie LIST
kolorki = kolory #kopiowanie listy
#kolorki = list(kolory)
kol = kolorki[:]

#KROTKA = TUPLE
animal = ("pies", "kot", "zmija")
"""
niemutowalna
stosowanie jest jako atrybuty FUNKCJI na wejsciu i na wyjsciu;
reprezentacja rekordu z TABELI (np z SQL)
"""

#ZBIÓR = SET
"""
nie jest uporządkowany, nie jest indeksowany,
teoria zbiorów - unikatowość, niepowtarzalne elementy
"""
drzewa = {"buk", "jesion", "dab", "sosna", "baobab"}

print(type(drzewa))

print(drzewa)
print(drzewa)
#print(drzewa[1]) #nie działą, bo nie jest indeksowany

for d in drzewa: #można iterować elementy, mimo że nie jest indksowany
    print(d)

drzewa.add("dab") #dodanie takiego samego składnika - jezeli juz jest to nie dodaje

#zastosowanie zbioru = setu
nb = [1,2,4,2,6,5,8,6,4,3,5,45] #trzeba zrobic liste unikatowa, dzieki SET
print(nb)
nb = list(set(nb)) #przeksztalcamy liste nb na SET, a potem znowu na liste
print(nb)


print("\n\n-------SŁOWNIK =DISCTIONARY-----------\n")
#SŁOWNIK =DISCTIONARY
"""
para key:value
"""

samochod = {
    "marka" : "Opel",
    "model" : "Vectra",
    "rok" : "2006",
}
print(samochod)
print(type(samochod))

print("--------")
for k, v in samochod.items():
    print(k, v)
print("--------")
for s in samochod:
    print(samochod[s])
print("--------")
print(samochod.items()) #TUPLE wewnatrz DICTa
print("--------")
for k, v in samochod.items():
    print(f"{k}, {v}")
print("--------")
