import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passwords(num_passwords, length):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords

print("Passwortgenerator")

length = int(input("Gib die Länge der Passwörter ein: "))
num_passwords = int(input("Gib die Anzahl der zu erzeugenden Passwörter ein: "))
passwords = generate_passwords(num_passwords, length)

print("Generierte Passwörter:")

for password in passwords:
    print(password)