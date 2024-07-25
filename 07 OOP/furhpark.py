class Auto:
    def __init__(self, hersteller, kennzeichen, fahrgestellnummer, kilometerstand=0):
        self.__hersteller = hersteller
        self.__kennzeichen = kennzeichen
        self.__fahrgestellnummer = fahrgestellnummer
        self.__kilometerstand = kilometerstand
        self.__tueren_geschlossen = True
        self.__ausgeliehen_von = None
 
    def tuerenBetaetigen(self):
        self.__tueren_geschlossen = not self.__tueren_geschlossen
 
    def fahren(self, kilometer):
        if self.__tueren_geschlossen:
            self.__kilometerstand += kilometer
            print(f"Das Auto fährt {kilometer} Kilometer. Neuer Kilometerstand: {self.__kilometerstand}")
        else:
            print("Die Türen sind nicht geschlossen!")
   
    def getKennzeichen(self):
        return self.__kennzeichen
 
class Mitarbeiter:
    def __init__(self, personalnummer, name):
        self.__personalnummer = personalnummer
        self.__name = name
        self.__ausgeliehenes_auto = None
 
    def auto_ausleihen(self, auto):
        self.__ausgeliehenes_auto = auto
        print(f"{self.__name} hat das Auto mit Kennzeichen {auto.getKennzeichen()} ausgeliehen.")
       
auto1 = Auto("Lamborghini", "WÜ U 36", "928491", "5162")
auto2 = Auto("Mercedes-Benz", "WÜ U 37", "6925191", "45478")
mitarbeiter1 = Mitarbeiter("123456", "Leon Mustermann")
mitarbeiter2 = Mitarbeiter("987654", "Max Mustermann")
 
#Beim Mitarbeiter 2 wird die Methode auto_ausleihen aufgerufen und als Parameter die Referenz auf das Auto1 mitgegeben
mitarbeiter2.auto_ausleihen(auto1)
