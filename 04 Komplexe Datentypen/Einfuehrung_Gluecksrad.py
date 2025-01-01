from random import randint

zufallszahlen = []
nutzerZahlen = []

for x in range(0,6):
    zufallszahl = randint(1,42)
    zufallszahlen.append(zufallszahl)

print(zufallszahlen)

for n in range(0,6):
    nutzerZahl = int(input("Zahl eingeben: "))
    nutzerZahlen.append(nutzerZahl)

gleicheZahlen = []
 
for x in nutzerZahlen:
    if x in zufallszahlen:
        #doesnt work - to check
        #if(x not in zufallszahlen):
            gleicheZahlen.append(x)
 
size =len(gleicheZahlen)
 
print("Diese Zahlen sind gleich: " , gleicheZahlen)
print("So viele Zahlen sind gleich: " , size)