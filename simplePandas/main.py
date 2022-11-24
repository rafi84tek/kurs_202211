"""


"""

import numpy as np
import pandas as pd

#seria danych
s = pd.Series([2, 5, 6, np.nan, 9, 12, 45])
print(s)

daty = pd.date_range("20221124", periods=6) #periods = okresy
daty = pd.date_range("20221124", periods=6, freq= "M") #periods = okresy
print(daty)
print("------------------------------------------------------")
# print(daty2)
# print("------------------------------------------------------")

#data Frame
ramka = pd.DataFrame(np.random.randn(6, 4), index = daty, columns = list("ABCD")) #tworzenie losowej macierzy 6x4
#z opisem kolumn ABCD i opsiem wierszy (daty z listy DATY)
print(ramka)
print("------------------------------------------------------")
print(ramka.head(3)) #wyświetlanie tylko pierwsze 3 rekordy
print(ramka.tail(2)) #wyświetlanie tylko ostatnich 2 rekordów
print("------------------------------------------------------")
print(ramka.index) #opis wierszy
print(ramka.columns) # opis kolumn
print("------------------------------------------------------")
npramka = ramka.to_numpy() #dane do przekazania do NumPy
print(npramka)
print("------------------------------------------------------")
print(ramka.describe()) #dane statystyczne dla kolumn
print("------------------------------------------------------")
print(ramka.T) #transpozycja ramki
print("------------------------------------------------------")
print(ramka.sort_index(axis=1, ascending=False)) #sortowanie, odwrócenie kolejności kolumn DCBA
print("------------------------------------------------------")
print(ramka.sort_index(axis=0, ascending=False)) #sortowanie, odwrócenie kolejności wierszy dat
print("------------------------------------------------------")
print(ramka.sort_values(by="B")) #sortowanie po wartościach z kolumny B
print("------------------------------------------------------")
print(ramka["A"]) #wydruk tylko kolumny A
print("------------------------------------------------------")
print(ramka[:3]) #wydruk 3 pierwszych wierszy
print("------------------------------------------------------")
print(ramka["20221130":"20230331"])
print("------------------------------------------------------")
print(ramka.loc[daty[0]]) #filtr dla daty pierwszej, wchodzi funkcjąLOC
print(ramka.loc[daty[0:2]]) #filtr dla daty pierwszej od 0 do 2 (nie uwzględniając 2),
print("------------------------------------------------------")
print(ramka.loc[:,["A","B"]]) #filtr na wszystkie daty, ale kolumny tylko A i B
print("------------------------------------------------------")
print(ramka.loc["20221130":"20230331" ,["A"]]) #filtr na  daty z zakresu, ale kolumny tylko A
print("------------------------------------------------------")
y = ramka.loc[daty[1], "C"]
print(y)
print("--------------------iloc----------------------------------")
print(ramka.iloc[3])
print("------------------------------------------------------")
print(ramka.iloc[3:5, 0:2]) # wiersz 3 i 4, kolumny 0 i 1
print("------------------------------------------------------")
print(ramka.iloc[[1,3,5], [1,3]]) # wiersz 2, 4 i 6, kolumny 2 i 4
print("------------------------------------------------------")
print(ramka[ramka["A"]>0]) #tylko wiersze z kolumną A, gdzie A > 0
print("------------------wstawienie NaN w miesjce niepasujące do kryterium------------------------------------")
print(ramka[ramka > 0])
print("------------------------------------------------------")

print("\n------------------------------------------------------")
print("----------panda CSV--------------------------------------------")
print("------------------------------------------------------\n")
print("----------import pliku CSV--------------------------------------------")
osoba = pd.read_csv("zdrowie.csv")
print(osoba)
print(type(osoba))
print("---------eksport Data Frame do CSV---------------------------------------------")
ramka.to_csv("mojaramka.csv")
print("--------eksport Data Frame do DICT----------------------------------------------")
aa = ramka.to_dict()
print(aa)
print("------------------------------------------------------")
