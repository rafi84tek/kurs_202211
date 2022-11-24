"czytanie CSV"
"Wiersze w CVS nie mogą być puste!!"

import csv

with open("firma.csv", encoding="utf-8") as pc:
    csv_reader = csv.reader(pc, delimiter=";")
    licznik_wierszy = 0
    for wiersz in csv_reader:
        if licznik_wierszy == 0:
            print(f"nazwa kolumny: {', '.join(wiersz)}")
        else:
            print(f'\t{wiersz[0]} pracuje na stanowisku {wiersz[1]} ma urodziny w miesiącu {wiersz[2]}'
                  f' i otrzymuje nagrodę w wysokości {wiersz[3]} zł.')
        licznik_wierszy += 1
    print(f'Dodano {licznik_wierszy} linii.')
    print(f'Dodano {licznik_wierszy-1} osób.')

