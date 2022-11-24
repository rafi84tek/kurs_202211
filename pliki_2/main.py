import os

f = open("dane.txt","r", encoding="utf-8")
"parametr encoding jest gdzieś dalego w parametrach, więc wymienianimy go literalnie"

print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")

print(type(f))
print(f.closed) #plik z danymi nie został zamknięty
f.close()
print(f.closed)


print("__________________________")
"czytanie całego pliku"

f = open("dane.txt", "r", encoding="utf-8")
print(f.read())
f.close()


print("__________________________")
"czytanie całego pliku poprzez pętlę"
f = open("dane.txt", "r", encoding="utf-8")
for linia in f:
    print(linia, end="")
f.close()


print("__________________________")
"czytanie całego pliku"
f = open("dane.txt", "r", encoding="utf-8")
g = f.read()
f.close()
print(g)
print(g.splitlines())


print("__________________________")
f = open("message.txt", "a", encoding="utf-8")
# "a" - append, dopisuje do pliku
f.write("to jest ważna informacja.\n")
f.close()


print("__________________________")
f = open("message.txt", "r", encoding="utf-8")
print(f.read())
f.close()


print("__________________________")
# usuwanie plików
if os.path.exists("message.txt"):
    os.remove("message.txt")
    print("plik został usunięty")
else:
    print("plik nie istnieje")


