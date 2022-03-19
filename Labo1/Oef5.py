KLEIN = 0.12
GROOT = 0.25
aantalkleine = int(input("Geef het aantal kleine flessen : "))
aantalgrote = int(input("Geef het aantal grote flessen : "))
print(f"{round((KLEIN * aantalkleine) + (GROOT * aantalgrote),2)} EUR")