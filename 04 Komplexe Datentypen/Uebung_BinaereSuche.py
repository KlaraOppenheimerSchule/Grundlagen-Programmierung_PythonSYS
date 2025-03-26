kundennummern = [14000, 10001, 13000, 12345, 10156, 11000, 10023, 15000, 10234, 10345]
suche = int(input("Welche Kundennummer wollen Sie suchen? "))
kundennummern = sorted(kundennummern)

def Suchen(array, suchwert):

    while len(array) > 1:

        mitte = int(len(array) / 2)

        if array[mitte] == suchwert:
            return True
        elif array[mitte] > suchwert:
            array = array[0:mitte]
        else:
            array = array[mitte:len(array)]
    return False

print(Suchen(kundennummern,suche))