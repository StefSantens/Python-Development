DIEREN = {0 : "Aap",
            1 : "Haan",
            2 : "Hond",
            3 : "Varken",
            4 : "Rat",
            5 : "Os",
            6 : "Tijger",
            7 : "Konijn",
            8 : "Draak",
            9 : "Slang",
            10 : "Paard",
            11 : "Geit"}

jaar = int(input("Geef een jaar : "))
print(DIEREN[jaar%12])