class rezept:
    def __init__(self, name, zubereitungszeit, text, zutaten):
        self.__name=name
        self.__zubereitungszeit=zubereitungszeit
        self.__text=text
        self.__zutaten= zutaten

    def kalorienBerechnen(self):
        kalorienInDerSumme=0
        for zutat in self.__zutaten:
            kalorienInDerSumme=kalorienInDerSumme+zutat.getKalorien()
        print(self.__name)
        print(kalorienInDerSumme)

class zutat:
    def __init__(self, name, kalorien, menge):
        self.__name=name
        self.__kalorien=kalorien
        self.__menge=menge

    def getKalorien(self):
        return self.__kalorien


zutat1=zutat("Spaghetti", 65, 200)
zutat2=zutat("Tomatensosse", 155, 100)
zutaten=[]
zutaten.append(zutat1)
zutaten.append(zutat2)
nudelrezept=rezept("Spaghetti mit Tomatensosse", 30, "Zuerst muss man ...", zutaten)
nudelrezept.kalorienBerechnen()


zutatneu1 = zutat("Eier", 77, 6)
zutatneu2 = zutat("Mehl", 15, 300)
zutatneu3 = zutat("Milch", 45, 200)

zutatenneu=[]
zutatenneu.append(zutatneu1)
zutatenneu.append(zutatneu2)
zutatenneu.append(zutatneu3)

kuchenrezept=rezept("Eierkuchen", 65, "Zuerst müssen die Eier...", zutatenneu)
kuchenrezept.kalorienBerechnen()
