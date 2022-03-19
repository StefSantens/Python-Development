def format(text, length):
    out = ""
    if(len(text) > length):
        out = text
    else:
        x = (length - len(text)) //2
        for i in range(x):
            out +=" "
        out+=text
        for i in range(x):
            out +=" "
    return out

text = input("Geef tekst : ")
karakters = int(input("Geef het aantal karakters : "))
print(format("hallo",10))