from random import randint

Zufallszahl=int(randint(1,10))
print(Zufallszahl)
UserZahl=(int(input("Denke dir eine ganzzahlige Zahl zwischen 1 und 10 aus: ")))

if UserZahl!=Zufallszahl:    
    if (UserZahl<Zufallszahl):   
        UserZahl2=int(input("Zahl war zu niedrig. Rate noch einmal: "))   
        if (UserZahl2 == Zufallszahl):   
            print("Richtig geraten")
        else:  
            print(f"{UserZahl} war die gesuchte Zahl. Leider alle Versuche verbraucht")    
   
    if (UserZahl>Zufallszahl):   
        UserZahl2=int(input("Zahl war zu hoch. Rate noch einmal: "))   
        if (UserZahl2 == Zufallszahl):   
            print("Richtig geraten")
        else:  
            print(f"{UserZahl} war die gesuchte Zahl. Leider alle Versuche verbraucht")    
   
else:
    print("Richtig geraten! Es wurde 1 mal geraten.")
 
