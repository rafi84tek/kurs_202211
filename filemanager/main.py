"""
menader do obsługi plików

"""

class FileManager:
    #obowiązkowe funkcje init, enter, exit

    def __init__(self, filename, mode, encod):
        print("Inicjacja funkcji init()")
        #init decyduje o tym, co będąmogły zrobić ENTER i EXIT
        self.filename = filename
        self.mode = mode
        self.encod = encod
        self.file = None

    def __enter__(self):
        print("Inicjacja funkcji enter()")
        self.file = open(self.filename, self.mode, encoding = self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Inicjacja funkcji exit()")
        self.file.close()

#utwrozenie pliki i zapisanie tekstu
with FileManager('test.txt', 'w', 'utf-8') as f:
    print("Blok wykonawczy w instrukcji with")
    f.write("to jest test managera")
print(f.closed)
print("---------------------------------")

#odczyt pliku
with FileManager('test.txt', "r", 'utf-8') as f:
    print(f.read())
print("---------------------------------")

