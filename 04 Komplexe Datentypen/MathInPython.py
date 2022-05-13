from cmath import pi

meinPI=pi

def multiplizieren (x, meinPi):
    ergebnis=x*x*meinPI
    return ergebnis

radius=int(input())

ergebnis=multiplizieren(radius, meinPI)
print(ergebnis)

