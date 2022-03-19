def verzending(aantal):
    prijs = 0
    if(aantal >= 1):
        prijs +=8.5
        prijs += (3*(aantal -1))
    return prijs
aantal = int(input("Geef aantal artikelen : "))
print(verzending(aantal))