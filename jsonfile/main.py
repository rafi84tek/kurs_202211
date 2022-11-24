"""
JSON

"""

import json
print("-------JSON------------------------------------")
# jsonsource = '{"imie":"Olga", "nazwisko":"Kot", "wiek":34, "miasto":"Kraków", "liczba_punktow":88.9}'
jsonsource = '{"imiona":["Olga", "Maria","Kunegunda"], "nazwisko":"Kot", "wiek":34, "miasto":"Kraków", "liczba_punktow":88.9}'
print(jsonsource)
print(type(jsonsource))

print("-------parsowanie pliku JSON------------------------------------")
#parsowanie pliku JSON
y = json.loads(jsonsource)
print(y)
print(type(y))
print(y["imiona"][1])
print("-------------------------------------------")

print("-------zrobienie JSON z słownika------------------------------------")
samochod = {
    "marks":"Opel",
    "model":"Insignia",
    "rok":2018,
    "poj":1.9,
}
jsonauto = json.dumps(samochod,indent=4)
print(jsonauto)

print("-------zapisanie JSON do pliku------------------------------------")
with open("sam.json", "w", encoding='utf-8') as f:
    f.write(jsonauto)

print("-------odczyt pliku JSON------------------------------------")
with open("sam.json", "r", encoding="utf-8") as f:
    ad = json.load(f)
print(ad)
print("-------------------------------------------")
