#1
#import pathlib
#print("Das ist das aktuelle Verzeichnis: ", pathlib.Path().absolute())

#2
import math
print(math.pi)

#3
from datetime import date
today=date.today()
print(today)

#4
from random import randint
print(randint(0,100))

#5
import statistics
zahlen=1,4,8,12
durchschnitt=statistics.mean(zahlen)
print(durchschnitt)

