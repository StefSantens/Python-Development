dagen = int(input("Aantal dagen : "))
uren = int(input("Aantal uren : "))
minuten = int(input("Aantal minuten : "))
seconden = int(input("Aantal seconden : "))
print(f" Totaal aantal seconden : {seconden + (minuten * 60) + (uren *60*60) + (dagen*60*60*24)}")