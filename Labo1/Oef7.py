RENTE = 1.2
bedrag = float(input("Geef bedrag op bankrekening : "))
for x in range(1,4):
    bedrag = bedrag * RENTE
    print(f" Jaar {x} : {round(bedrag * RENTE,2)}")