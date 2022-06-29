#Aufgabe 1

#Aufgabe 2

#Aufgabe 3

#Aufgabe 4
import os
from os import listdir

print("C:\Test\Scans")

dateien = os.listdir(r"C:\Test\Scans")

for datei in dateien:
    print(datei)
    dateiMitPfad= os.path.join("C:\Test\Scans", datei)
    print(dateiMitPfad)
    os.remove(dateiMitPfad)

#Aufgabe 5
# datei.__sizeof__

#Aufgabe 6
