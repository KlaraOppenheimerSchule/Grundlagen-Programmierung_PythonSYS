tage = 0
 
lohn = 1
 
gesamtlohn = 0 
 
while gesamtlohn < 40000:
    tage = tage+1
    gesamtlohn = gesamtlohn+lohn
    lohn = lohn*2
print("Sie brauchen" ,tage, "Tage")