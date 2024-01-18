       
# TODO: Noch gegen Aufgabenstellung hin prüfen
year=int(input("Jahr eingeben"))
if(year % 4 == 0):
    if(year % 100 != 0):
        print("Schaltjahr")
    elif(year % 400 == 0):
        print("Schaltjahr")
    else:
        print("Kein Schaltjahr")
else:
    print("Kein Schaltjahr")
