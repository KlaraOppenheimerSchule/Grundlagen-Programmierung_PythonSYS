def pass_eingabe():
    user_pass = input().upper()
    return user_pass
    
user_pass=pass_eingabe()

print(len(user_pass))

while (len(user_pass) != 6):
    user_pass=pass_eingabe()
    print(len(user_pass))

print(user_pass)