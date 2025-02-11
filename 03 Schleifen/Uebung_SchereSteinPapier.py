import random

win1 = 0
win2 = 0

while win1 < 3 and win2 < 3:
    s1 = random.randint(1, 3)
    s2 = random.randint(1, 3)
    # 1=Schere
    # 2=Stein
    # 3=Papier

    if s1 == s2:
        print(f"Unentschieden! Stand: {win1} zu {win2}")
    elif (s1 == 1 and s2 == 3) or (s1 == 2 and s2 == 1) or (s1 == 3 and s2 == 2):
        win1 += 1
        print(f"Punkt für Spieler 1! Stand: {win1} zu {win2}")
    else:
        win2 += 1
        print(f"Punkt für Spieler 2! Stand: Spieler1: {win1} Spieler2: {win2}")

print(f"Spielende! Spieler1: {win1} Spieler2: {win2}")
