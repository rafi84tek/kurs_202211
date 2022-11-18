"""
Fukcje

"""
print("------------------")
def witaj(name):
    return f"Milo Cie widziec {name}."

witaj("Rafal")
print(witaj("Rafal"))
print(witaj("Ola"))

print("------------------")

def konkurs(imie, punkty):
    return f"uczestnik {imie}, liczba punktow {punkty}"

print("------------------")
# def osoba(funkcja, name): #funkcja bez nawiasu (), bo nie uruchamiany tu funkcji
#     return funkcja(name) #funkcja od funkcji = funkcja wyzszego rzędu
# modyfikowana wersja ponizej,bierze dowolna liczbe argumentow, ale musza byc w danej kolejnosc
def osoba(funkcja, *args): #*args to dowolna liczba argumentow, ktore beda przechwytywane
    return funkcja(*args)

print(witaj("Adas"))
print(osoba(konkurs, "Ula", 78))

print("\n\n------------------")
def rejestracja(oplata): #funcka z funkcjami wewnatrz
    def lista():
        return "jestes na liscie zawodnikow"
    def brak():
        return "jesli nie zaplacisz za start w ciagu 3 dni zostaniesz usuniety z listy"
    def error():
        return "wpisz 1 - wplata lub 0 - brak"

    if oplata == 1:
        return lista #przekazanie funkcji dalej, bez je uruchamania
    elif oplata == 0:
        return brak
    else:
        return error()

print(rejestracja(1)()) #tu dopiero uruchamiamy funkcje dla LISTA
print(rejestracja(0)()) #tu dopiero uruchamiamy funkcje dla BRAK
print(rejestracja(10)) #tu funkcja ERROR była uruchomiona już przy RETURN, bo tam miała nawiasy

print("\n\n------------------\n")

n = 67 #globalny
print(n)
def policz(a, b, x):
    global n #jezeli takie cos wpiszemy, to od teraz N jest GLOBALNE, nie da sie juz tego zmienic
    n = (a+b)*x+n
    return n

print(policz(7,6,2))
# print(n) #nie wiedac jej, bo jest wewnatrz, ale trzeba to delkarowac
print("\n\n--------funkcja ANONIMOWA----------\n")
#funkcja ANONIMOWA
"""
bez nazwy, wykonywane tu i teraz, np. LAMBDA
"""

print("\n\n------lambda------------\n")
print((lambda a,b,c:a+b-c)) #info ze to funkcja
print((lambda a,b,c:a+b-c)(3,1,2)) #w dodatkowym nawiasie podajemy parametry
print("\n\n-------lambda x-----------\n")
x = lambda e,m:e*(m-1)
print(x)
print(x(4,2))
"""
co to daje?
stosowana do prostych przeksztalcen
"""

g = sum([i**3 for i in range(1000000)]) #tu jest funkcja anoniomowa, list comprehension
print(g)

# filtrowanie listy LB i przejeie tylko parzystych
lb = [45, 23, 12, 12, 46, 67, -1, -100, 56]
print(lb)
np = list(filter(lambda x:x%2==0, lb)) #FILTER sprawdza True/False, wtedy przekazuje dalej lub nie
print(np)

#to samo ale w formie funkcji
def warunek(x):
    return x%2==0

_np = list(filter(warunek, np))
print(_np)

#przeksztalcenie listy LB na x^3 do nowej listy CUBE
cube = list(map(lambda x:x**3, lb))
print(cube)

