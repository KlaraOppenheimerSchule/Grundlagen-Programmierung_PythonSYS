import os
#Aufgabe 1
# Geben Sie den Dateinamen an, der gelöscht werden soll
datei_name = "example_file.txt"

if os.path.exists(datei_name):
    os.remove(datei_name)
    print(f"Die Datei '{datei_name}' wurde erfolgreich gelöscht.")
else:
    print(f"Die Datei '{datei_name}' existiert nicht.")


#Aufgabe 2
datei_name = "Report"
# Überprüfen, ob die Datei existiert
if os.path.exists(datei_name):
    # Datei löschen, wenn sie existiert
    os.remove(datei_name)
    print(f"Die Datei '{datei_name}' existierte und wurde gelöscht.")
else:
    print(f"Die Datei '{datei_name}' existierte nicht.")

# Datei erstellen
with open(datei_name, 'w') as f:
    f.write("Dies ist eine neue Report-Datei.")
    print(f"Die Datei '{datei_name}' wurde erfolgreich erstellt.")

#Aufgabe 3
import shutil

# Pfad zum Dokumentenverzeichnis des aktuellen Nutzers
dokumenten_verzeichnis = os.path.expanduser("~/Documents")

# Name des Zielverzeichnisses
ziel_verzeichnis = os.path.join(dokumenten_verzeichnis, "Textdateien")

# Überprüfen, ob das Zielverzeichnis existiert, und bei Bedarf erstellen
if not os.path.exists(ziel_verzeichnis):
    os.makedirs(ziel_verzeichnis)
    print(f"Das Verzeichnis '{ziel_verzeichnis}' wurde erstellt.")
else:
    print(f"Das Verzeichnis '{ziel_verzeichnis}' existiert bereits.")

# Alle Dateien im Dokumentenverzeichnis durchlaufen
for datei_name in os.listdir(dokumenten_verzeichnis):
    # Überprüfen, ob die Datei die Endung .txt hat
    if datei_name.endswith(".txt"):
        # Vollständigen Dateipfad erstellen
        voller_datei_pfad = os.path.join(dokumenten_verzeichnis, datei_name)
        if os.path.isfile(voller_datei_pfad):
            # Datei in das Zielverzeichnis kopieren
            shutil.copy(voller_datei_pfad, ziel_verzeichnis)
            print(f"Die Datei '{datei_name}' wurde nach '{ziel_verzeichnis}' kopiert.")

print("Alle .txt-Dateien wurden erfolgreich kopiert.")


#Aufgabe 4
print("C:\Test\Scans")
dateien = os.listdir(r"C:\Test\Scans")

for datei in dateien:
    print(datei)
    dateiMitPfad= os.path.join("C:\Test\Scans", datei)
    print(dateiMitPfad)
    os.remove(dateiMitPfad)

#Aufgabe 5
if(os.path.isdir("C:/Users/Zobel/Desktop/Testordner")):
    pass
else:
    os.makedirs("C:/Users/Zobel/Desktop/Testordner")

os.replace("C:/Users/Zobel/Desktop/Testordner", "C:/Users/Zobel/Testordner")


#Aufgabe 6
dateien = os.listdir(r"C:\Users\Zobel\Documents\Mensaplan")

for datei in dateien:
    dateiMitPfad= os.path.join("C:/Users/Zobel/Documents/Mensaplan", datei)
    #Hier ist noch eine kleine Änderung erforderlich
    if(os.path(dateiMitPfad.__sizeof__)) > 100:
        os.remove.dateiMitPfad
        print("Datei gelöscht")
    else:
        print("Datei nicht gelöscht")
