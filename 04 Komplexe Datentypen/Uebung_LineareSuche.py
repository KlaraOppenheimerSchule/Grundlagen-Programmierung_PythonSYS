kundennummern = [10001, 10023, 10156, 10234, 10345, 11000, 12345, 13000, 14000, 15000]
suche = int(input("Welche Kundennummer wollen Sie suchen? "))

gesuchtenWertGefunden=False

for x in kundennummern:
    if x == suche:
        gesuchtenWertGefunden=True

if gesuchtenWertGefunden==True:
    print("Die Kundennummer ist in der Liste!")
else:
    print("Die Kundennummer ist leider nicht in der Liste :(")