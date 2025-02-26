from random import randint
 
zufallszahlen=[]
eingabezahlen=[]
 
#Auswertung von innen nach außen:
#randint erzeugt eine Zufallszahl
#append fügt diese der Liste zufallszahlen hinzu
#zufallszahlen.append(randint(0,24))
#zufallszahlen.append(randint(0,24))
#zufallszahlen.append(randint(0,24))
#zufallszahlen.append(randint(0,24))
#zufallszahlen.append(randint(0,24))
#zufallszahlen.append(randint(0,24))
 
#Alternativ eine Schleife bauen, die 6 Zufallszahlen erzeugt und in der Liste ablegt
 
#len ermittelt die aktuelle Anzahl der Elemente in der Liste
#Zu Beginn 0 Elemente, dann 1 Element...
while (len(zufallszahlen) <6):
    zufallszahl=randint(1,24)
    if(zufallszahl not in zufallszahlen):
        zufallszahlen.append(zufallszahl)
 
while(len(eingabezahlen) <6):
    eingabezahl=int(input("Zahl: "))
    #Prüfung ob eingabezahl doppelt ist und im richtigen Zahlenbereich
    if(eingabezahl not in eingabezahlen and (eingabezahl > 0 and eingabezahl <25)):
        eingabezahlen.append(eingabezahl)
    else:
        print("Eingabezahl im falschen Zahlenbereich oder bereits vorhanden.")
 
    #Alternative Kurzschreibweise:
    #eingabezahlen.append(int(input("Zahl: ")))
 
print(zufallszahlen)
print(eingabezahlen)
#Nutzer soll 6 Zahlen zwischen 0 und 24 eingeben
 
 
#Überprüfung, wie viele richtig geratene Zahlen vorhanden sind
 
anzahlRichtige=0
 
for gerateneZahl in eingabezahlen:
    if(gerateneZahl in zufallszahlen):
        anzahlRichtige=anzahlRichtige +1
 
#Ausgabe der Anzahl der Richtigen
print(anzahlRichtige)