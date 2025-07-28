import time
import gc

passwörter = []

def Passwort_save(passwörter):
    stark = False
    while not stark:
        passwort = input("Was ist dein Passwort? ")
        if not len(passwort) == 6 or not passwort.isalpha() or not passwort.isupper() or passwort in passwörter:
            print("Entspricht nicht den Bedingungen oder ist schon verhanden")
            stark = False
        else:
            stark = True
    return passwort

def bruteforce(passwörter):
    zurordnung={
        0:"A",
        1:"B",
        2:"C",
        3:"D",
        4:"E",
        5:"F",
        6:"G",
        7:"H",
        8:"I",
        9:"J",
        10:"K",
        11:"L",
        12:"M",
        13:"N",
        14:"O",
        15:"P",
        16:"Q",
        17:"R",
        18:"S",
        19:"T",
        20:"U",
        21:"V",
        22:"W",
        23:"X",
        24:"Y",
        25:"Z"
    }
    guess = [0,0,0,0,0,0]
    geraten = False
    counter = 0
    while geraten==False:
        counter = counter +1
        passwort = ""
        for i in range(len(guess)):
            passwort=passwort+zurordnung[guess[i]]
        print(passwort)
        if passwort in passwörter:
            print("ACCESS GRANTED")
            geraten=True
        else:
            guess[5]=guess[5]+1
            guess.reverse()
            for x in range(len(guess)):
                if guess[x]>25 and x != 5:
                    guess[x]=guess[x]-26
                    guess[x+1]=guess[x+1]+1
                elif guess[5] > 25:
                    break
            guess.reverse()
        gc.collect()
    return counter, passwort

for i in range(3):
    passwörter.append(Passwort_save(passwörter))
print(passwörter)
start = time.time()
counter, passwort=bruteforce(passwörter)
end = time.time()
print(f"Das Passwort {passwort} wurde in {counter} versuchen erraten. Dauer: {round(((end - start)/60), 2)} Minuten")