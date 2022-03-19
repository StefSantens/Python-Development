tekst = input("Geef de boodschap : ")
getal = int(input("Geef het ceasar getal : "))
output = ""
for i in tekst:
    if(ord(i) in range(96,123) or range(64,91)):
        if(getal > 0):
            if(96 <= ord(i) + getal <= 122 or 64<=ord(i) + getal <=90):
                output+=chr(ord(i)+getal)
            else:
                output+=chr(ord(i) +getal - 26)
        else:
            if(96 <= ord(i) + getal <= 122 or 64<=ord(i) + getal <=90):
                output+=chr(ord(i)+getal)
            else:
                output+=chr(ord(i) +getal + 26)
    else:
        output = i
print(output)
