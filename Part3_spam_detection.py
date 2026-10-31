nume_fisier = input('Introdu numele fisierului: ')

suma = 0
numar = 0

try:
    fisier = open(nume_fisier, 'r')

    for linie in fisier:
        if linie.startswith('X-DSPAM-Confidence:'):
            valoare = float(linie.split(':')[1])
            suma = suma + valoare
            numar = numar + 1

    fisier.close()

    if numar > 0:
        media = suma / numar
        print('spam confidence scor:', media)
    else:
        print('Nu au fost gasite valori spam pentru a genera scor-ul.')
except FileNotFoundError:
    print('Eroare: fisierul nu exista!')
