#Aufgabe: Erstellen Sie ein Notenprogramm, dass schrittweise folgende Funktionen erfüllt:
#   a) Einlesen und Speichern von beliebig vielen Noten vom Nutzer, bis dieser nichts mehr eingibt.
#   b) Sicherstellen bei der Eingabe, dass Noten im Bereich von 1-6 liegen.
#   c) Ermittlung der schlechtesten vorhandenen Noten und Ausgaben dieser.
#   d) Ermittlung der besten vorhandenen Note und Ausgabe dieser.
#   e) Berechnung und Ausgabe von Notendurchschnitt der eingegebenen Noten.
#   f) Ausgabe der Häufigkeit des Vorkommens der Note 1.

#   a)
'''
noten = []
eingabe = 0
while eingabe != "":
    eingabe = input("Gib eine Schulnote ein: ")
    if(eingabe.isdigit()):
        noten.append(eingabe)

print(noten)

#   b)
noten = []
eingabe = 0
while eingabe != "":
    eingabe = input("Gib eine Schulnote ein: ")
    if eingabe.isdigit() and 1 <= int(eingabe) <= 6:
        noten.append(eingabe)

print(noten)
'''
'''

#   c)
noten = []
eingabe = 0
while eingabe != "":
    eingabe = input("Gib eine Schulnote ein: ")
    if eingabe.isdigit() and 1 <= int(eingabe) <= 6:
        noten.append(eingabe)

if not noten:
        print("Keine Noten eingegeben.")
else:
    schlechteste_note = max(noten)
    print("Die schlechteste Note ist:", schlechteste_note)

#   d)
noten = []
eingabe = 0
while eingabe != "":
    eingabe = input("Gib eine Schulnote ein: ")
    if eingabe.isdigit() and 1 <= int(eingabe) <= 6:
        noten.append(eingabe)

if not noten:
        print("Keine Noten eingegeben.")
else:
    beste_note = min(noten)
    print("Die beste Note ist:", beste_note)
    
#   Kombiniert c) und d)
noten = []
eingabe = 0
while eingabe != "":
    eingabe = input("Gib eine Schulnote ein: ")
    if eingabe.isdigit() and 1 <= int(eingabe) <= 6:
        noten.append(eingabe)

if not noten:
        print("Keine Noten eingegeben.")
else:
    beste_note = min(noten)
    print("Die beste Note ist:", beste_note)
    schlechteste_note = max(noten)
    print("Die schlechteste Note ist:", schlechteste_note)'''
'''
# Kombiniert c) und d) mit einem for-i-Schleife
noten = []
eingabe = 0

while eingabe != "":
    eingabe = input("Gib eine Schulnote ein: ")
    if eingabe.isdigit() and 1 <= int(eingabe) <= 6:
        noten.append(int(eingabe))

if not noten:
    print("Keine Noten eingegeben.")
else:
    beste_note = noten[0]
    schlechteste_note = noten[0]
    
    for note in noten:
        if note < schlechteste_note:
            schlechteste_note = note
        if note > beste_note:
            beste_note = note
    
    print("Die beste Note ist:", beste_note)
    print("Die schlechteste Note ist:", schlechteste_note)

#   e)
noten = []
eingabe = 0

while eingabe != "":
    eingabe = input("Gib eine Schulnote ein: ")
    if eingabe.isdigit() and 1 <= int(eingabe) <= 6:
        noten.append(int(eingabe))

print(noten)

if not noten:
    print("Keine Noten eingegeben.")
else:
    durchschnitt = sum(noten) / len(noten)
    print("Der Notendurchschnitt ist:", durchschnitt)
'''
#   f)
noten = []
eingabe = 0

while eingabe != "":
    eingabe = input("Gib eine Schulnote ein: ")
    if eingabe.isdigit() and 1 <= int(eingabe) <= 6:
        noten.append(int(eingabe))

print(noten)

if not noten:
    print("Keine Noten eingegeben.")
else:
    anzahl_note_1 = noten.count(1)
    print("Die Note 1 kommt", anzahl_note_1, "mal vor.")