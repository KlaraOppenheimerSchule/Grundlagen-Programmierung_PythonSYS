eingabe_stundenlohn = 0 
while eingabe_stundenlohn < 12:
    eingabe_stundenlohn = float(input("wie ist ihr stundenlohn:  "))
    if eingabe_stundenlohn < 12:
        print("Stundenlohn muss mindestens 12 Euro betragen")
 
eingabe_arbeitsstunden = float(input("wie is die anzahl der arbeitsstunden:  "))
 
berechnung_gesamtlohn = (eingabe_stundenlohn * eingabe_arbeitsstunden)
print(berechnung_gesamtlohn , "€")
 
if berechnung_gesamtlohn > 1000:
    print("Sie müssen ihr Einkommen beim Finanzamt anmelden!")