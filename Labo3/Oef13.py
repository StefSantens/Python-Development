def breuk(teller, noemer):
    x = True
    g = 0
    if(teller>noemer):
        g = noemer
    else:
        g = teller
    while(x):
        for i in range(2,g):
            if(teller %i == 0 and noemer%i==0):
                teller = teller/i
                noemer = noemer/i
                break
            else:
                x = False
    return f"{teller} / {noemer}"

print(breuk(6,27))