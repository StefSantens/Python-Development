from random import *


def passwoord():
    out = ""
    for i in range(randint(7,10)):
        out+=chr(randint(33,126))
    return out

# print(passwoord())