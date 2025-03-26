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
#2.	Prüfen Sie, ob es in aktuellem Verzeichnis eine Datei mit dem Namen „Report“ gibt. 
# Sofern nicht, legen Sie diese an. Sofern diese bereits existiert, löschen Sie diese zuvor. (**)

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
#3.	Kopieren Sie alle vorhandenen Dateien mit der Endung „txt“ aus dem Dokumentenverzeichnis des 
# aktuellen Nutzers in ein Unterverzeichnis mit dem Namen „Textdateien“. Prüfen Sie auch hier 
# wiederrum zuvor, ob das entsprechende Unterverzeichnis bereits existiert, und legen Sie dieses 
# bei Bedarf zuvor noch an. (**)

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
#4.	Stellen Sie sich folgendes Szenario vor: In einer Abteilung wird gemeinschaftlich ein Scanner 
# genutzt. Der netzwerktaugliche Scanner speichert alle gescannten Dokumente in einem speziellen 
# Ordner auf einem Netzwerklaufwerk ab. Unglücklicherweise vergessen verschiedene Kollegen, ihre 
# Scanunterlagen nach der Nutzung zu löschen. Ihre Aufgabe ist es, ein Skript zu schreiben, das 
# bei der Ausführung alle Dateien in diesem Ordern löscht. Aus Vereinfachungsgründen erzeugen Sie 
# sich einfach zuvor einem Ordern mit einigen exemplarischen Dateien. Dies müssen hierbei keine 
# PDF-Dateien seinen, TXT-Dateien genügen auch. Eventuell vorhandene Unterordner sollen ebenfalls 
# gelöscht werden. (***)

print("C:\Test\Scans")
dateien = os.listdir(r"C:\Test\Scans")

for datei in dateien:
    print(datei)
    dateiMitPfad= os.path.join("C:\Test\Scans", datei)
    print(dateiMitPfad)
    os.remove(dateiMitPfad)

#Aufgabe 5
#5.	Ein Kollege hat sich über Ihr eigenmächtiges Vorgehen beschwert. Nach heftigen Diskussionen 
# haben Sie vereinbart, alle Dateien vor der Löschung in einem auf der gleichen Ordnerebene 
# liegenden Ordner „Altscans“ zu verschieben. Sofern dieser Ordner noch nicht existiert, soll dieser 
# angelegt werden. (***)

if(os.path.isdir("C:/Users/Zobel/Desktop/Testordner")):
    pass
else:
    os.makedirs("C:/Users/Zobel/Desktop/Testordner")

os.replace("C:/Users/Zobel/Desktop/Testordner", "C:/Users/Zobel/Testordner")


#Aufgabe 6
#6.	Nachdem sich nun auch noch der Systembetreuer beschwert hat, dass das vereinbarte Verfahren zuviel 
# Speicherplatz verbraucht, haben Sie sich darauf verständigt, ein weiteres Skript zu schreiben, das 
# alle Dateien im Ordner „Altscans“ löscht, die größer als 100 KB sind. (***)

dateien = os.listdir(r"C:\Users\Zobel\Documents\Mensaplan")

for datei in dateien:
    dateiMitPfad= os.path.join("C:/Users/Zobel/Documents/Mensaplan", datei)
    #Hier ist noch eine kleine Änderung erforderlich
    if(os.path(dateiMitPfad.__sizeof__)) > 100:
        os.remove.dateiMitPfad
        print("Datei gelöscht")
    else:
        print("Datei nicht gelöscht")
