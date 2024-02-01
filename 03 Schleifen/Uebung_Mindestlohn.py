Mindestlohn=float(12.41)
StundenlohnG=float(input("Wie ist dein gewünschter Stundenlohn?"))

while StundenlohnG<Mindestlohn:    
    StundenlohnG=float(input("Der gewünschte Stundenlohn ist nicht der Mindestlohn oder höher. Bitte nocheinmal eingeben!"))

Arbeitsstunden=float(input("Wie viele Stunden willst du arbeiten?"))
    
Gesamtlohn=StundenlohnG*Arbeitsstunden
print(Gesamtlohn) 

if (Gesamtlohn>1000):     
    print("Dein Einkommen ist größer als 1000€. Du musst das dem Finanzamt melden!")