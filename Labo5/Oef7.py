som = 0
getal = input("Geef een getal : ")
while getal !="":
    try:
        som+=int(getal)
        print(som)
    except:
        print("De ingevoerde waarde was geen getal")
    finally:
        getal = input("Geef een getal : ")