zahlen = [11, 4, 17, 9, 6, 20]
gerateneZahlen = [4, 4, 6, 2, 12, 22]
gleicheZahlen = []
 
for x in gerateneZahlen:
    if x in zahlen:
        gleicheZahlen.append(x)
 
size =len(gleicheZahlen)
 
print("Diese Zahlen sind gleich: " , gleicheZahlen)
print("So viele Zahlen sind gleich: " , size)