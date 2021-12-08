import random
 
print ("Choose a number between 1 and 10!")
 
nutzerZahl=int(input())
rdmZahl=random.randint(1,10)
 
while nutzerZahl > 10 or nutzerZahl < 0:
    print ("That's not between 1 and 10.")
    nutzerZahl=int(input())
    if nutzerZahl == rdmZahl:
        print ("Impressive! :) \nnumber: "+str(nutzerZahl)+"\nVersuche: 1")
 
if nutzerZahl == rdmZahl:
    print ("Impressive! :) \nnumber: "+str(nutzerZahl)+"\nVersuche: 1")
 
elif nutzerZahl != rdmZahl:
    if nutzerZahl < rdmZahl:
        print ("Sorry, that's too low.\nTry again!")
        eingabe=int(input())
        if nutzerZahl == rdmZahl:
            print ("Nice! :) \nnumber: "+str(rdmZahl)+"\nVersuche: 2")
        elif nutzerZahl != rdmZahl: 
            print ("You lose :( \nnumber: "+str(rdmZahl))
    elif nutzerZahl > rdmZahl:
        print ("Sorry, that's too high.\nTry again!")
        eingabe=int(input())
        if nutzerZahl == rdmZahl:
            print ("Nice! :) \nnumber: "+str(rdmZahl)+"\nVersuche: 2")
        elif nutzerZahl != rdmZahl: 
            print ("You lose :( \nnumber: "+str(rdmZahl))