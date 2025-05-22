class rezept:
    def __init__(self, name, zubereitungszeit, text):
        self.__name=name
        self.__zubereitungszeit=zubereitungszeit
        self.__text=text
        self.__zutaten= []
        self.__zutaten.append(zutat("Spaghetti", 65, 200))
        self.__zutaten.append(zutat("Tomatensosse", 155, 100))

    def kalorienBerechnen(self):
        kalorienInDerSumme=0
        for zutat in self.__zutaten:
            kalorienInDerSumme=kalorienInDerSumme+zutat.getKalorien()
        
        print(kalorienInDerSumme)

class zutat:
    def __init__(self, name, kalorien, menge):
        self.__name=name
        self.__kalorien=kalorien
        self.__menge=menge

    def getKalorien(self):
        return self.__kalorien

nudelrezept=rezept("Spaghetti mit Tomatensosse", 30, "Zuerst muss man ...")
nudelrezept.kalorienBerechnen()

