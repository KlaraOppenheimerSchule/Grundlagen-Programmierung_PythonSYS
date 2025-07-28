class PC:
    def __init__(self, hersteller, baujahr, modell, angeschaltet):
        self.__hersteller = hersteller
        self.__baujahr = baujahr
        self.__modell = modell
        self.__angeschaltet = angeschaltet

    def hochfahren(self):
        if self.__angeschaltet:
            print("PC ist ausgeschaltet")
            self.__angeschaltet = False
        else:
            print("PC ist angeschaltet")

    def getHersteller(self):
        print(self.__hersteller)

# Arraylist erzeugen

class Notebook(PC):
    def __init__(self, hersteller, baujahr, modell, angeschaltet, akkulaufzeit):
        super().__init__(hersteller, baujahr, modell, angeschaltet)
        self.akkulaufzeit= akkulaufzeit


pcs = []

# Drei Objekte auf Basis der Klasse PC erzeugen
pc1 = PC("Lenovo", "2019", "LegionY520", True)
pc2 = PC("Lenovo1", "2018", "LegionY521", True)
pc3 = PC("Lenovo2", "2017", "LegionY522", True)

# PCs der Arraylist hinzufügen
pcs.append(pc1)
pcs.append(pc2)
pcs.append(pc3)

# Jeden PC aus der Arraylist pcs hochfahren
for pc in pcs:
    pc.hochfahren()
    pc.hochfahren()

notebook1= Notebook("Lenovo2", "2017", "LegionY522", True,300)
notebook1.getHersteller()