def dagen(maand, jaar):
    maand = maand-1
    dagen = [31,30,31,30,31,30,31,31,30,31,30,31]
    if(jaar %400 == 0):
        if(maand == 1):
            out = 29
        else:
            out = dagen[maand]
    elif(jaar %100 == 0):
        out = dagen[maand]
    elif(jaar %4==0):
        if(maand == 1):
            out = 29
        else:
            out = dagen[maand]
    else:
        out = dagen[maand]
    return out
def main():
    maand = int(input("Geef de maand : "))
    jaar = int(input("Geef het jaar : "))
    print(dagen(maand, jaar))
