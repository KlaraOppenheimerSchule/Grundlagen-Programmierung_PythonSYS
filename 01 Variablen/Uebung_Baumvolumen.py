import math

d=float(input("Was ist der Durchmesser in Centimeter: "))
l=float(input("Was ist die Länge in Meter: "))

volumen=float(((math.pi/4)*(d**2))*l/10000)

print(volumen)
