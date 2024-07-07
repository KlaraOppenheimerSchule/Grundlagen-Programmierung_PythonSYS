drei_Achsen = [12.50, 14.60, 15.70, 19.80, 19.80, 20.80]
vier_Achsen = [13.10, 15.20, 16.30, 19.40, 20.40, 21.40]

abfrage_achsen = int(input("Wie viele Achsen hat dein LKW: "))
eingabe_schadstoffklasse = input("Gib eine Schadstoffklasse ein: ")
eingabe_schadstoffklasse = eingabe_schadstoffklasse.upper
eingabe_km = int(input("Gib die gefahrenen Kilomenter ein: "))

def mautberechnung(drei_achsen, vier_achsen, achsen, schadstoffklasse, km):
    indexstelle=0
    if schadstoffklasse == "A":
        indexstelle = 0
    if schadstoffklasse == "B":
        indexstelle = 1
    if schadstoffklasse == "C":
        indexstelle = 2
    if schadstoffklasse == "D":
        indexstelle = 3
    if schadstoffklasse == "E":
        indexstelle = 4
    if schadstoffklasse == "F":
        indexstelle = 5
    
    if achsen <= 3:
        mautjekm = drei_achsen[indexstelle]
    
    else:
        mautjekm = vier_achsen[indexstelle]
    
    summe = mautjekm * km/100
    return summe

ergebnis = mautberechnung(drei_Achsen, vier_Achsen, abfrage_achsen, eingabe_schadstoffklasse, eingabe_km)

print(f"Für deine Strecke zahlst du {ergebnis}€ Mautgebühren")

