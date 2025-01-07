from random import randint

#Sechs Zufallszahlen vom Computer erzeugen lassen
zufallszahlen = []

for x in range(0,6):
    zufallszahl = randint(1,42)
    zufallszahlen.append(zufallszahl)

print(zufallszahlen)

#Sechs Zahlen vom Nutzer eingeben lassen
nutzerZahlen = []

for n in range(0,6):
    nutzerZahl = int(input("Zahl eingeben: "))
    nutzerZahlen.append(nutzerZahl)


#Ermitteln, wie viele Zahlen richtig erraten wurden
gleicheZahlen = []
 
for x in nutzerZahlen:
    if x in zufallszahlen:
        if(x not in gleicheZahlen):
            gleicheZahlen.append(x)
 
size =len(gleicheZahlen)
 
print("Diese Zahlen sind gleich: " , gleicheZahlen)
print("So viele Zahlen sind gleich: " , size)