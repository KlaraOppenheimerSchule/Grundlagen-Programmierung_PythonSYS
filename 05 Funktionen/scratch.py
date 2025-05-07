def addNumber(zahl1, zahl2, zahl3):
    ergebnis=zahl1+zahl2+zahl3 
    return ergebnis

ersteZahl=int(input("Zahl 1:"))
zweiteZahl=int(input("Zahl 2:"))
dritteZahl=int(input("Zahl 3:"))

ruckgabewert=addNumber(ersteZahl,zweiteZahl,dritteZahl)
print(str(ruckgabewert))