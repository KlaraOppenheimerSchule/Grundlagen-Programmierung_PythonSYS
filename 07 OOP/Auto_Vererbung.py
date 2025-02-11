class Fahrzeug:
    def __init__(self, anzahlReifen):
        self.__anzahlReifen=anzahlReifen
    
    def signalGeben(self):
        print("ring,ring")

class Flugzeug():
    def testMethode():
        pass

class Auto(Fahrzeug, Flugzeug):
    def __init__(self, hersteller, kennzeichen, fahrgestellnummer, kilometerstand=0):
        self.__hersteller = hersteller
        self.__kennzeichen = kennzeichen
        self.__fahrgestellnummer = fahrgestellnummer
        self.__kilometerstand = kilometerstand
        self.__tueren_geschlossen = True
        self.__ausgeliehen_von = None
    
    #Überschriebene Methode
    def signalGeben(self):
        print("TutTut")

 

    def tuerenBetaetigen(self):
        self.__tueren_geschlossen = not self.__tueren_geschlossen
 

    def tuerenBetaetigen(self, staerke):
        pass

    def fahren(self, kilometer):
        if self.__tueren_geschlossen:
            super.__init__
            self.__kilometerstand += kilometer
            print(f"Das Auto fährt {kilometer} Kilometer. Neuer Kilometerstand: {self.__kilometerstand}")
        else:
            print("Die Türen sind nicht geschlossen!")
   
    def getKennzeichen(self):
        return self.__kennzeichen
 
auto1 = Auto("Lamborghini", "WÜ U 36", "928491", "5162")
auto1.signalGeben()
auto1.tuerenBetaetigen()

