# Aufgabe 7:

def zinsberechnung(kapital, zinssatz, zinstage):
    zinsen = (kapital * zinssatz * zinstage) / (100 * 360)
    return zinsen

kapital = float(input("Gib das Kapital ein: "))
zinssatz = float(input("Gib den Zinssatz ein: "))
zinstage = int(input("Gib die Anzahl der Zinstage ein: "))

berechnete_zinsen = zinsberechnung(kapital, zinssatz, zinstage)

print("Die berechneten Zinsen betragen:", berechnete_zinsen)