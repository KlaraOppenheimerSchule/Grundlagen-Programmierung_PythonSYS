
alter = int(input("Bitte Alter eingeben"))

while alter < 101:
    if(alter % 2 == 0):
        print ("Alter ist rund: ", alter)
    alter=alter+1
