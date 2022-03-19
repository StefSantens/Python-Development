def mediaan(een, twee, drie):
    list = [een, twee, drie]
    list.sort()
    return list[1]
een = int(input("Geef een getal : "))
twee = int(input("Geef een getal : "))
drie = int(input("Geef een getal : "))
print(mediaan(een, twee, drie))