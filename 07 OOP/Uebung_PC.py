class PC:
    def __init__(self, hersteller, baujahr, modell, angeschaltet):
        self.hersteller = hersteller
        self.baujahr = baujahr
        self.modell = modell
        self.angeschaltet = angeschaltet
    def hochfahren(self):
        if self.angeschaltet:
            print("PC ist ausgeschaltet")
            self.angeschaltet = False
        else:
            print("PC ist angeschaltet")

# Arraylist erzeugen

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