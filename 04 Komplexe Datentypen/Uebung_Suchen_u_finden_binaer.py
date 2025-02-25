kundennummern = [14000, 10001, 13000, 12345, 10156, 11000, 10023, 15000, 10234, 10345]

gesuchterWert = int(input("Welche Kundennummer wollen Sie suchen? "))

kundennummern = sorted(kundennummern)

startBereichsindex=0
endBereichsindex=len(kundennummern) - 1

gesuchtenWertGefunden=False

while startBereichsindex <= endBereichsindex:
    mitte = (startBereichsindex + endBereichsindex) // 2
    mitte_wert = kundennummern[mitte]

    if mitte_wert == gesuchterWert:
        gesuchtenWertGefunden = True
        break
    elif gesuchterWert > mitte_wert:
        startBereichsindex = mitte + 1
    else:
        endBereichsindex = mitte - 1

print(f"Ist die Kundennummer {gesuchterWert} in der Liste vorhanden? {gesuchtenWertGefunden}")