#1 Sie erhalten den Auftrag einen komplexen Datentyp zu erzeugen und in diesem ihre vier Wunschnoten 
#im Fach AeUP zu speichern. Legen Sie diesen komplexen Datentyp in der Programmiersprache Ihrer Wahl inklusive der Wunschnoten an. (1P)

noten=[4,6,2,1,4,6,6];

# Lassen Sie nun mit Hilfe einer Schleife den Durchschnitt der Noten berechnen. Natürlich soll die 
# Berechnung bei einer unterschiedlichen Anzahl von Noten funktionieren. 

summe=0
for note in noten:
    summe=summe + note

notendurchschnitt= summe/len(noten)
print(str(notendurchschnitt))


# Löschen Sie nun alle Noten aus dem komplexen Datentyp, die schlechter als der Durchschnitt sind. 
"""
for note in noten:
   if(note > notendurchschnitt):
       print("Removing "+str(note))
       noten.remove(note)

for note in noten:
    print(str(note))

#Funktionierende Lösung

noten_copy=noten[:]
for note in noten_copy:
   if(note > notendurchschnitt):
       print("Removing "+str(note))
       noten.remove(note)

for note in noten:
    print(str(note))
"""

# Ermitteln Sie nun, welche Note sich am häufigsten in der Liste befindet. Geben Sie dieses inklusive deren 
# Anzahl aus. 

count1=0
count2=0
count3=0
count4=0
count5=0
count6=0

for note in noten:
    if(note==1):
        count1=count1+1
    if(note==2):
        count2=count2+1
    if(note==3):
        count3=count3+1
    if(note==4):
        count4=count4+1
    if(note==5):
        count5=count5+1
    if(note==6):
        count6=count6+1


hoechsteZahl=0
hoechsterNennung=0

if(count1 >hoechsterNennung):
    hoechsterNennung=count1
    hoechsteZahl=1

if(count2 > hoechsterNennung):
    hoechsterNennung=count2
    hoechsteZahl=2

if(count3 >hoechsterNennung):
    hoechsterNennung=count3
    hoechsteZahl=3

if(count4 >hoechsterNennung):
    hoechsterNennung=count4
    hoechsteZahl=4

if(count5 >hoechsterNennung):
    hoechsterNennung=count5
    hoechsteZahl=5

if(count6 >hoechsterNennung):
    hoechsterNennung=count6
    hoechsteZahl=6

print("Höchste Zahl: "+ str(hoechsteZahl) + " Anzahl: " + str(hoechsterNennung) )
