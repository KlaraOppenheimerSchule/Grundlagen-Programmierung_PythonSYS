import os
#Aufgabe 1

#Aufgabe 2

#Aufgabe 3

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
