from os import system


def taxi(afstand, weekend, nacht, luchthaven):
    out = 2.9
    if(luchthaven ==True):
        out+=78
        if(afstand > 50):
            out+=(afstand - 50)*2
        return out
    if(nacht == True):
        out+=2.5
    if(weekend == True):
        if(1<afstand<5):
            out += 2.5*afstand
        if(6<afstand<20):
            out += 2.3*afstand
        if(afstand>21):
            out += 2.1*afstand
        return out
    else:
        if(1<afstand<5):
            out += 2.5*afstand
        if(6<afstand<20):
            out += 2.2*afstand
        if(afstand>21):
            out += 2.0*afstand
        return out

print(taxi(25,False,False,False))