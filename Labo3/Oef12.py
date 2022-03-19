from Oef10 import passwoord
from Oef11 import wachtwoord

while(True):
    password = passwoord()
    print(password)
    if(wachtwoord(password)):
        break