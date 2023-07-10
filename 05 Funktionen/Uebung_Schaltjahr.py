def schaltjahr(jahr):
    if jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0):
        return True
    else:
        return False

jahr = int(input("Gib ne Jahreszahl ein: "))

if schaltjahr(jahr):
    print("Passt, das Jahr", jahr, "is' ein Schaltjahr.")
else:
    print("Ne, das Jahr", jahr, "is' kein Schaltjahr.")