# Citim numere pana cand utilizatorul scrie "done"

suma = 0
numar_valori = 0

while True:
    text = input("Introdu un numar (sau 'done' pentru a termina): ")

    if text == "done":
        break

    try:
        numar = float(text)
    except ValueError:
        print("Eroare! Te rog introdu un numar.")
        continue

    suma = suma + numar
    numar_valori = numar_valori + 1

print("Suma numerelor este:", suma)
print("Numarul de valori introduse este:", numar_valori)

if numar_valori > 0:
    media = suma / numar_valori
    print("Media numerelor este:", media)
else:
    print("Nu ai introdus niciun numar, deci nu putem calcula media.")
