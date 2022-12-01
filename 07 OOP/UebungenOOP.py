import math

# Aufgabe 1
zeichenfolge = "bAcKuP.tXt"
zeichenfolge_klein = zeichenfolge.lower()
print(zeichenfolge_klein)

#Aufgabe 2
print(zeichenfolge_klein.__contains__("txt"))

#Aufgabe 3 
print(zeichenfolge_klein.find("."))

#Aufgabe 4 
print(zeichenfolge_klein.replace(".",","))

#Aufgabe 5
zahl1 = int(input("Bitte geben sie Zahl 1 ein"))
zahl2 = int(input("Bitte geben sie Zahl 2 ein"))
print(zahl1**zahl2)
print(math.pow(zahl1,zahl2))

#Aufgabe 6
class rechner:
    def __init__(self, cpu, gpu, ram):
        self.__cpu = cpu
        self.__gpu = gpu
        self.__ram = ram
        
    def setcpu(self,x):
        self.cpu = x
        
    def setgpu(self,x):
        self.gpu = x
        
    def setram(self,x):
        self.ram = x
        
    def geteigenschaft(self):
        print(self.cpu, self.gpu, self.ram)
        

pc1 = rechner("AMD","3070","8GB")
pc2 = rechner("Intel","3080","16GB")
pc3 = rechner("Intel","2070","32GB")

list_rechner = [pc1,pc2,pc3]

for i in list_rechner:
    i.geteigenschaft()