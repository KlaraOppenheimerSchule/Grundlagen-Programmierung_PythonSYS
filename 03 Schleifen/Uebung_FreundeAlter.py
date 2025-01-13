gesamtalter = 0
i = 1

while i <= 4:
    alter = int(input("Bitte geben Sie das Alter ein: "))
    if alter <= 0:
        print("Falsche Eingabe")
    else:
        gesamtalter += alter
        i += 1
    
durchschnittsalter = gesamtalter / 4
print("Das Durchschnittsalter ist:", durchschnittsalter)