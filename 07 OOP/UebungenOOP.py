import math

# Aufgabe 1
zeichenfolge = "bAcKuP.tXt"
zeichenfolge_klein = zeichenfolge.lower()
print(zeichenfolge_klein)

#Aufgabe 2
print(zeichenfolge_klein.__contains__("txt"))

#Aufgabe 3 
print(zeichenfolge_klein.find("."))

#Aufgabe 4 
print(zeichenfolge_klein.replace(".",","))

#Aufgabe 5
zahl1 = int(input("Bitte geben sie Zahl 1 ein"))
zahl2 = int(input("Bitte geben sie Zahl 2 ein"))
print(zahl1**zahl2)
print(math.pow(zahl1,zahl2))