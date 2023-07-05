def LKWMaut(schadstoffklasse, raeder, km):
    mautTabelle = [{'A': 12.5, 'B': 14.6, 'C': 15.7, 'D': 18.8, 'E': 19.8, 'F': 20.8},
                    {'A': 13.1, 'B': 15.2, 'C': 16.3, 'D': 19.4, 'E': 20.4, 'F': 21.4}]
    if raeder <= 3:
        preis = float( mautTabelle[0][schadstoffklasse] )
    else:
        preis = float( mautTabelle[1][schadstoffklasse] )
    return preis * km
print("Bitte geben Sie ihre Schadstoffklasse ein:")
schadstoffklasse = input()
print("Bitte geben Sie ihre Raeder-Anzahl ein:")
raeder = float(input())
    
print("Bitte geben sie ihre km ein:")
km = float(input())
maut = LKWMaut(schadstoffklasse, raeder, km)
print ("Ihre Maut ist: ", maut)