# Aufgabe

# Ein Nutzer erstellt grundsätzlich in einer CSV-Datei Vokabeln.
# Die CSV-Datei beinhaltet in der linken Spalte das deutsche Wort
# und in der rechten Spalte die englische Übersetzung hiervon.
# Das Porgramm das zu erstellen ist, ermöglicht das Anlegen und Ändern
# der Vokabelliste nicht. Dies erfolgt außerhalb des zu erstellenden Programms.

# Das Programm liest jedoch die CSV-Datei ein und bietet dem Nutzer an,
# einen Vokabeltest durchzuführen. Hierbei wird dem Nutzer eine deutsche
# angezeigt und dieser muss diese übersetzen. Wenn ein Nutzer eine Vokabel eingibt.
# wird überprüft, ob diese von diesem korrekt übersetzt wurde. Sofern
# diese falsch übersetzt wird, wird die richtige Übersetzung angezeigt.

import csv
import random

def check_translation(Deutsch, Englisch):
    user_input = input(f"Bitte übersetze '{Deutsch}' ins Englische: ").lower()
    return user_input == Englisch.lower()

file_name="05 Funktionen\Vokabeln.csv"

vocabulary = []

with open(file_name, "r", encoding="utf-8") as file:
    vocabulary = list(csv.reader(file, delimiter=","))

random.shuffle(vocabulary)
schon_gefragt = []

for row in vocabulary:
    Deutsch = row[0]
    Englisch = row[1]
    if Deutsch not in schon_gefragt:
        while True:
            if check_translation(Deutsch, Englisch):
                print("Ja, korrekt!")
                break
            else:
                print(f"Leider nicht richtig! Die korrekte Übersetzung lautet: {Englisch}")
        schon_gefragt.append(Deutsch)
