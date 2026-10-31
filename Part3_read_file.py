
nume_fisier = input('Introdu Numele fisierului dorit: ')

try:
    fisier = open(nume_fisier, 'r')
    for linie in fisier:
        print(linie.upper(), end='')
    fisier.close()
except FileNotFoundError:
    print('Eroare: fisierul nu exista!')
