#1
import os
print("Das ist das aktuelle Verzeichnis: ", os.listdir())

#2
import math
print(math.pi)

#3
from datetime import *
today=date.today()
print(today)

#4
year=today.year
print(year)

#5
from random import randint
print(randint(0,100))

#6
import statistics
zahlen=1,4,8,12
durchschnitt=statistics.mean(zahlen)
print(durchschnitt)

wert=round(2.33)
print(wert)

#7 
import os
liste=os.listdir()
for i in liste:
    if os.path.isdir(i):
        print("Ordner: ", i)


