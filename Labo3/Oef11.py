def wachtwoord(password):
    out = True
    if(len(password) < 8):
        out = False
    if(password.islower()):
        out = False
    if(password.isupper()):
        out = False
    if(not any(char.isdigit() for char in password)):
        out = False
    return out

# print(wachtwoord("hahahhaHa"))