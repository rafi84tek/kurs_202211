"""
pierwszy projekt z NumPy - Num1
"""
print("\n\n----------------------------")
import numpy as np

print("\n\n--------array--------------------")
a = np.array([1,3,6,8,3,46,234,2])
print(a)
print(type(a))

print("\n\n--------srednia arytmetyczna--------------------")
sa = a.mean() #srednia arytmetyczna
print(sa)

print("\n\n--------macierz / tablica--------------------")
a2d = np.array([[3,4,5],[9,11,2],[98,45,2]])
print(a2d)

print("\n\n--------tensor / tablica 3D--------------------")
a3d = np.array([[[12,13],[9,45]],[[87,34],[23,65]],[[45,45],[67,23]]])
print(a3d)

print("\n\n--------array z określeniem typu wartosci--------------------")
ae = np.array([3,8,11], dtype=np.float64)
print(ae)

print("\n\n--------wektor zerowy, do wyzerowania wartosci--------------------")
z = np.zeros(45)
print(z)

print("\n\n--------wektor jedynkowy--------------------")
j = np.ones(16)
print(j)

print("\n\n--------wektor empty - losowane wartosci w okolicy zera--------------------")
em = np.empty(19)
print(em)

print("\n\n--------lista od:do z krokiem = w przedziale 2-84, co 4--------------------")
h1 = np.arange(2, 89, 4)
print(h1)

print("\n\n---------lista z podzialem przedzialu od:do i przez co dzielic-------------------")
h2 = np.linspace(0, 10, num=5)
print(h2)

print("\n\n--------tablica - sortowanie--------------------")
arr = np.array([5,16,7,9,34,0,23,56,2,5,7])
print(arr)
# print(sorted(arr))
print(arr.sort()) #modyfikacja tablicy w miejscu
print((arr)) #wydruk zmodyfikowanej tablicy

print("\n\n--------tablica - konkatenacja--------------------")
k = np.array([4,8,7,1])
print(k)
p = np.array([2,3,16,7])
print(p)
d = np.array([3,5])
print(d)
g = np.concatenate((k, p, d))
print(g)

print("\n\n--------tablica - konkatenacja wymiarowa--------------------")
k1 = np.array([[1,2],[1001,544]])
p1 = np.array([[8,9],[3,6]])
g1 = np.concatenate((k1,p1), axis=0) #jezeli axis=1, to sklada tablice  inaczej, rowna liczba skladnikow
print(g1)

print("\n\n----------------------------")
print("--------SHAPES--------------------")
q = np.arange(6)
print(q)

print("--------RESHAPES--------------------")
#stosowane np. do odbudowania spłaszczonej warstwy
p = q.reshape(2,3)
print(p)

print("\n\n----------------------------")
print("--------indeksowanie tablic - zasady jak przy zwyklych listach--------------------")
dn = np.array([1,2,3])
print(dn[1])
print(dn[0:2])
print(dn[-2:])

print("\n\n----------------------------")
print("-----filtrowanie macierzy-----------------------")
tb = np.array([[1,4,7,9],[8,11,10,23],[2,8,11,30]])
print(tb[tb>11])

print("-----filtrowanie macierzy - warunek na zewnatrz-----------------------")
v = (tb>=9)
print(tb[v])

print("-----filtrowanie macierzy - z warunkiem na liczby parzyste, warunek odrazu w obiekcie-----------------------")
parzyste = tb[tb%2==0]
print(parzyste)

print("--------zastosowanie kryteriów, by okreslic skladniki ktore chcemy otrzymac-------------------")
v2 = (tb>=9) | (tb==1)
print(v2) #maciez z wynikiem oceny, czy spełnia czy nie spełnia naszych kryteriów
print(tb[v2]) #wyniki ktore spelnily nasze warunki
""" tu moge sprobowac zrobic funkcje ktore zwroci macierz tb w postaci wyniku jak v2, ale z wartosciami liczbowymi a nie True/False"""

print("--------zastosowanie kryteriów, by okreslic skladniki ktore chcemy otrzymac, inna wersja-------------------")
v3 = (tb>=9) & (tb<19)
print(tb[v3])

print("\n\n----------------------------")
print("---------------------------")
w = np.array([1,2,4,5,7,8,9,10,12,14])
print(w)
w1 = w[3:8]
print(w1)

print("---------------------------")
# big_arr = np.arange(1, 1e450,2) #ValueError: Maximum allowed size exceeded
# print(big_arr)

print("------przekształcenie ARANGE + RESHAPE---------------------")
x = np.arange(1,25).reshape(2,12) #zakres 1-24, przeksztalcony do tabeli 2-12, dwa wiersze po 12 elementow
print(x)




print("---------operacje na macierzach------------------")
print("---------------------------")
print("---------   - dodawanie list------------------")
dt = np.array([1,2])
ns = np.ones(2, dtype=int)
print(dt+ns)

print("---------    - dodawanie macierzy------------------")
m1 = np.array([[1,1], [2,2]])
m2 = np.array([[3,4], [1,7]])
print(m1+m2)

print("---------    - odejmowanie macierzy------------------")
print(m1-m2)

print("---------    - mnożenie macierzy------------------")
print(m1*m2)

print("---------    - dzielenie macierzy------------------")
print(m1/m2)

print("---------     - sumowanie macierzy, po osiach------------------")
print(m1.sum(axis=0)) #sumowanie w kolumnach
print(m1.sum(axis=1)) #sumowanie w wierszach

print("---------    - mnożenie macierzy przez współczynnik------------------")
print(m1*2.75)

print("---------    - element max/min, średnia z macierzy  ------------------")
m3 = m1*2.75
print(m3.max())
print(m3.min())
print(m3.mean())

print("---------    - funkcja zwracajaca element max/min, średnia z macierzy  ------------------")
# funkcja ktora zbiera elementy statystyki
def statystyki(macierz):
    minimum = np.min(macierz)
    maximum = np.max(macierz)
    sr_art = np.mean(macierz)
    rozstep = maximum - minimum
    return minimum, maximum, sr_art, rozstep

wynik = statystyki(m3)
print(wynik)
print("---------")
mini,maxi,sa,roz = statystyki(m3) #krotka zwrócona przez RETURN jest rozwinieta do 4 zmiennych (obiektów)
print(f"wartosc najwieksza: {maxi}, wart najmniejsza: {mini}, srednia aryt: {sa}, rozstep: {roz}")

print("\n---------    - funkcja wyciagajaca dowolny element z macierzy  ------------------")
def element(macierz, i, j):
    print(macierz[i,j])

element(m3, 0, 1)

print("---------")


print("\n\n---------generatory------------------")
#na potrzeby importujemy:
from numpy.random import default_rng
rng = default_rng()
vals = rng.standard_normal(10) #różne standardy do wyboru
print(vals)

