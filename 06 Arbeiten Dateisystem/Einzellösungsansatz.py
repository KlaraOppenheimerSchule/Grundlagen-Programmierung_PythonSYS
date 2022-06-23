import os
from os import listdir
print("C:\Test\Scans")
dateien = os.listdir(r"C:\Test\Scans")
for datei in dateien:
    print(datei)
    dateiMitPfad= os.path.join("C:\Test\Scans", datei)
    print(dateiMitPfad)
    os.remove(dateiMitPfad)