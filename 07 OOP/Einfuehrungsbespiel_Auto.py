class Auto:

    #Konstruktor
    def __init__(self, hersteller, modell, baujahr, leistung, verbrauch):
        self.__hersteller = hersteller
        self.__modell = modell
        self.__baujahr = baujahr
        self.__leistung = leistung
        self.__verbrauch = verbrauch
        self.__tuerZu = True

    #Methode der Klasse. Jedes Objekt verfügt dann über diese Methoden
    def tuerSchliessen(self):
        if(self.__tuerZu == True):
            print("Tür ist bereits geschlossen")

        else:
            self.__tuerZu = True
            print("Tür wurde geschlossen")

    def tuerOeffnen(self):
        if(self.__tuerZu == True):
            self.__tuerZu = False
            print("Tür wurde geöffnet")

        else:
            self.__tuerZu = False
            print("Tür ist bereits offen")

#------------

#Erzeugung eines Objektes, basierend auf der Klasse Auto. Aufruf des Konstruktors
meinAuto = Auto("Audi", "A4", 2015, 150, 4.5)

meinAuto.tuerOeffnen()
meinAuto.tuerSchliessen()
