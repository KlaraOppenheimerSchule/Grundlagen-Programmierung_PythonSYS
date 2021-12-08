user = "admin"
pas = "admin"

inp1 = input("Username eingeben: ")
inp2 = input("Passwort eingeben: ")

if (inp1.lower() == user.lower() and inp2 == pas):
    print("Zugriff gewährt")
else:
    print("Zugriff verweigert")