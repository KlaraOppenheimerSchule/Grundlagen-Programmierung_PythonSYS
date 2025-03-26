#Variable Liste
listeVonZahlen=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

#schleife für liste 
for zahl in listeVonZahlen:
    #Prüfe ob zahl ohne rest teilbar ist 
    if (zahl%2==0):
        print(zahl)

#zeile 11 ist außerhalb der schleif, da nicht mehr eingerückt ist
print("ende")
