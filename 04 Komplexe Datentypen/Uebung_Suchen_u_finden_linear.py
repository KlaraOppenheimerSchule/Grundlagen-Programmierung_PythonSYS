kundennummern = [10001, 10023, 10156, 10234, 10345, 11000, 12345, 13000, 14000, 15000]

gesuchterWert = int(input("Welche Kundennummer wollen Sie suchen? "))

gesuchtenWertGefunden=False

for kundennummer in kundennummern:
    if kundennummer == gesuchterWert:
        gesuchtenWertGefunden=True

if gesuchtenWertGefunden==True:
    print("Die Kundennummer ist in der Liste!")
else:
    print("Die Kundennummer ist leider nicht in der Liste :(")