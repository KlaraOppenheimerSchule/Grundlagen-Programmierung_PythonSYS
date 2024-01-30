# Kopfgesteuerte Schleifen (for-Schleife) in Python
# Zähle eine Zahl von 0 bis 10 hoch

# for-Schleife (Zählt automatisch hoch)
for i in range(11):
    print(i)

# Alternativ: while-Schleife (Zählt nicht automatisch hoch, y muss im Code erhöhrt werden)
y = 0
while y < 11:
    print(y)
    y += 1



# Foreach-Schleife ist in Python als for-Schleife bekannt und wird verwendet, um über Iterierbare zu iterieren
# In diesem Beispiel gibt es keine echte Notwendigkeit für eine foreach-Schleife, da die range-Funktion in Python die gleiche Funktionalität bietet

# Fußgesteuerte Schleifen (do-while und do-until) gibt es in Python nicht direkt, 
# daher verwenden wir while-Schleifen mit einer Bedingung am Anfang oder am Ende.

# Do-while-Äquivalent in Python
i = 0
while True:
    print(i)
    i += 1
    if i >= 11:
        break

# Do-until-Äquivalent in Python
i = 0
while True:
    print(i)
    i += 1
    if i > 10:
        break


