mensenjaar = int(input("Geef het aantal mensenjaren : "))
hondenjaar = mensenjaar *7
if(mensenjaar <= 2):
    hondenjaar = mensenjaar * 5,25
if (mensenjaar >= 2):
    hondenjaar = (mensenjaar-2)*4 + 10.5
print(f"{mensenjaar} jaar is gelijk aan {hondenjaar} honden jaren")