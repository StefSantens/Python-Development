letter = input("Geef letter : ")
if(len(letter) > 1):
    print("te veel karakters in letter")
elif(letter in [ "a", "e", "i", "o", "u"]):
    print("letter is een klinker")
elif(letter == "y"):
    print("letter is soms klinker, soms medeklinker")
else:
    print("letter is een medeklinker")