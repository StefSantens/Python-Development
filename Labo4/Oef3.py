list = []
woord = input("Geef een woord : ")
while(woord != ""):
    list.append(woord)
    woord = input("Geef een woord : ")
print("\nList\n")
for i in list:
    print(i)
print("\nSet\n")
for i in set(list):
    print(i)