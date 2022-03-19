from Oef8 import priem

def volgend_priemgetal(getal):
    x = True
    while(x):
        getal=getal+1
        if(priem(getal)):
            x = False
    return getal

print(volgend_priemgetal(13))