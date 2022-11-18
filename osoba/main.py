"""
OBIEKTY - częśc 3

"""

"""
tworzymy osobe - superdefinicje, ktora bedzie stanowila czesc wspolna dla kojenmych osob
- stan - konstruktor, np tabela w bazie danych
- zachowanie - fukcje

klasa jest modelem, instancja jest obiektem z cechami

"""

class Osoba:
    def __init__(self, imie, wiek, waga, wzrost=170): #funkcje specjalne, konstruktory klas, parametry sa zmienne,
        # uruchamiane podczas inicjacji, mozna podawac wartosci domyslne po zanku =
        self.imie = imie
        self.wiek = wiek
        self.waga = waga #self.waga moze byc np self.masa = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowy" #to jest stała
        self.info()

    def info(self):
        print("Utworzona nową osobę...")

    def print_osoba(self):
        print(f"osoba  ->  imię:{self.imie}, wiek: {self.wiek}, waga: {self.waga} kg, "
              f"wzrost: {self.wzrost} cm, kolor oczu: {self.kolor_oczu}")
    def wiekza10lat(self):
        return self.wiek+10

    def czypracownik(self):
        return False

    def bmi(self):
        return self.waga/(self.wzrost/100)**2

    def opis_bmi(self):
        if self.bmi() < 18.5:
            return "niedowaga"
        elif self.bmi() <=25:
            return  "waga prwidłowa"
        elif self.bmi() <= 30:
            return "nadwaga"
        else:
            return "otylosc"

os1 = Osoba("Jan", 44, 98, 180)
os1.kolor_oczu = "niebieskie" #zmiana koloru oczu
os1.print_osoba()
print(f"wiek za 10 lat: {os1.wiekza10lat()}")
print((f"Czy osoba jest pracowniekiem? {os1.czypracownik()}"))
print(f"bmi ciała :{os1.bmi():.2f}, opis: {os1.opis_bmi()}")

#hermetyzacja obiektow - zaden obiek nie wplywa na inny obiekt

print("----------------------------------")

os2 = Osoba("Olga", 14, 54, 160)
os2.print_osoba()
print(f"wiek za 10 lat: {os2.wiekza10lat()}")
print((f"Czy osoba jest pracowniekiem? {os2.czypracownik()}"))

print("----------------------------------")
# Tworzenie pracownika, na bazie klasy Osoba - dziedziczenie
class Pracownik(Osoba):
    def __init__(self, imie, wiek, waga, wzrost, firma, stanowisko, latapracy, wynagrodzenie):
        super().__init__(imie, wiek, waga, wzrost) #super(). odonosi się do klasy Osoba, można wpisać "Osoba.__init__", jawnie trzeba wypisać parametry
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie

    def print_pracownik(self):
        print(f"dane pracownika -> firma: {self.firma}, stanowisko pracy: {self.stanowisko}, "
              f"lata pracy: {self.latapracy}, wynagrodzneie: {self.wynagrodzenie}.")

    def czypracownik(self): #przesloniecie metody z Osoba
        return True


p1 = Pracownik("Piotr", 50,99,173,"ABC", "dyrektor", 12, 10600)
p1.print_osoba()
p1.print_pracownik()
print(f"wiek za 10 lat: {p1.wiekza10lat()}")
print((f"Czy osoba jest pracowniekiem? {p1.czypracownik()}"))

print("\n\n----------------------------------")
print("-------18.11.2022---------------------------")
print("----------------------------------\n")
# Tworzymy nowy CLASS - Student, z wielodziedziczeniem, ktory może być SPORTOWCEM, PRACOWNIKIEM, STUDENTEM
# ponieważ Pracownik juz dziedziczy Osobe, to nie musimy dziedziczyć Osobe, bo ona zwiera się w Pracowniku

class Sport:
    def __init__(self, dyscyplina, latauprawiania, best_wynik):
        self.best_wynik = best_wynik
        self.dyscyplina = dyscyplina
        self.latauprawiania = latauprawiania

    def infosport(self):
        print(f"dyscyplina: {self.dyscyplina}, lata uprawiana: {self.latauprawiania}, życiówka: {self.best_wynik}.")

class Empty: #pusta klasa, też działa, może być potrzebna w przyszłosci, kiedy kod coś do niej dopisze
    pass

#kolejność dziedizczonych klas nie jest ważna, ale zalecane
# wielodziedziczenie
# musimy wypisac tez SELF
class Student(Pracownik, Sport, Empty):
# ponizej beda pola w INIT
# pierwsza linia obowiazkowe zroimy,
# druga linia nieobowiazkowe
    def __init__(self, imie, wiek, waga, wzrost, nr_studenta, wydzial, kierunek, rok_stud,
                 firma="", stanowisko="", latapracy="", wynagrodzenie="", dyscyplina="", latauprawiania="", best_wynik=""):
        Pracownik.__init__(self, imie, wiek, waga, wzrost, firma, stanowisko, latapracy, wynagrodzenie)
        Sport.__init__(self, dyscyplina, latauprawiania, best_wynik)
        self.rok_stud = rok_stud
        self.kierunek = kierunek
        self.wydzial = wydzial
        self.nr_studenta = nr_studenta

    def print_student(self):
        print(f"Student ID: {self.nr_studenta}, wydzial: {self.wydzial}, kierunek {self.kierunek},"
              f"rok studiuw: {self.rok_stud}.")

    # czy jest pracownikiem?
    # jezeli wypełnione są pewne pola, to mozna wywnioskowac czy jest pracownikiem - np. wypełnienie pola FIRMA

    #przesłonięcie metody
    def czypracownik(self):
        return self.firma != "" #jezeli bedzie uzuoełniona FIRMA ot będzie TRUE


print("\n\n----------------------------------")
print("--------------Student - nie pracuje, nie jest sportowcem--------------------")
print("-------------- - nie jest Pracownikiem (False), nie jest sportowcem--------------------")
#Student, nie pracuje, nie jest sportowcem,
s1 = Student("Olaf", 22, 77, 180, 345345, "Budowlany", "Konstrukcja mostów", 3)
s1.print_osoba()
s1.print_student()
print(f"wiek za 10 lat: {s1.wiekza10lat()}")
print((f"Czy osoba jest pracowniekiem? {s1.czypracownik()}"))
print("----------------------------------\n")


print("\n\n----------------------------------")
print("--------------Student - pracuje, nie jest sportowcem--------------------")
print("-------------- -  jest Pracownikiem (True), nie jest sportowcem--------------------")
#Student, pracuje, nie jest sportowcem,
s2 = Student("Olga", 24, 55, 161, 34563, "Nauki Społeczne", "Socjologia", 4, "ABC", "sekretarka", 1, 2600)
s2.print_osoba()
s2.print_student()
s2.print_pracownik()
print(f"wiek za 10 lat: {s2.wiekza10lat()}")
print((f"Czy osoba jest pracowniekiem? {s2.czypracownik()}"))
print("----------------------------------\n")


print("\n\n----------------------------------")
print("--------------Student - nie pracuje, jest sportowcem--------------------")
print("-------------- -  nie jest Pracownikiem (False), jest sportowcem--------------------")
#Student, nie pracuje,  jest sportowcem,
# jawny zapisa atrybutow - dyscyplina=...
s3 = Student("Robert", 23, 88, 180, 987123, "Automatyka", "Informatyka", 3,dyscyplina="biegi ulltra",
             latauprawiania=5, best_wynik="102 km, 19g13m35s")
s3.print_osoba()
s3.print_student()
s3.infosport()
print(f"wiek za 10 lat: {s3.wiekza10lat()}")
print((f"Czy osoba jest pracowniekiem? {s3.czypracownik()}"))
print("----------------------------------\n")

# #kontrolowaie wprowadzanych danych:
# zarobek = input("podaj zarobek:")
# print(zarobek.isdigit()) #czy jest cyfrą?

# Dodajemy klasyfikacje BMI, musimy to dopisac w klasie Osoba
#  def bmi(self)
#  def opis_bmi(self)

