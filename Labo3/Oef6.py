from tkinter import Y


def Upper(text):
    out = text.capitalize()
    lijst = list(out)
    for i in range(len(text)-1):
        if(text[i] == "."):
            lijst[i+1] = out[i+1].upper()
    return "".join(lijst)

print(Upper("test dat eens.voor mij."))