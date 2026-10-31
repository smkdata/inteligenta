# Exercitiul 1 - Salariul brut
ore = input("Introdu numarul de ore: ")
rata = input("Introdu rata orara: ")
ore = float(ore)
rata = float(rata)
salariu = ore * rata
print("Salariul brut este:", salariu)

# Exercitiul 2 - Celsius in Fahrenheit
celsius = input("Introdu temperatura in Celsius: ")
celsius = float(celsius)
fahrenheit = celsius * 1.8 + 32
print("Temperatura in Fahrenheit este:", fahrenheit)

# Exercitiul 3 - Rezultate si tipuri
latime = 17
inaltime = 12.0

print("a:", latime // 2, type(latime // 2))
print("b:", latime / 2.0, type(latime / 2.0))
print("c:", inaltime / 3, type(inaltime / 3))
print("d:", 1 + 2 * 5, type(1 + 2 * 5))
