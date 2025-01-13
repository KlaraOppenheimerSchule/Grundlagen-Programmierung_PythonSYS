mindestlohn = 12.5
gesamtlohn = 0
nutzerabfrage = True

while nutzerabfrage:
    stundenlohn = float(input("\nBitte geben Sie ihren gewünschten Stundenlohn in € an\nIhre Eingabe: "))
    stundenanzahl = float(input("\nBitte geben Sie ihren gewünschten Stundenanzahl an\nIhre Eingabe: "))
    if stundenlohn > mindestlohn:
        gesamtlohn = (stundenlohn * stundenanzahl) * 4
        print("\nSie verdienen insgesamt", gesamtlohn,"€")
        if gesamtlohn > 1000:
            print("\nSie verdienen über 1000€ !\nBitte geben Sie ihr Einkommen beim Finanzamt an!")
        nutzerabfrage=False
     