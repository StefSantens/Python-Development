jaar = int(input("Geef een jaar : "))
if(jaar %400 == 0):
    print("Schrikkeljaar")
elif(jaar %100 == 0):
    print("Geen schrikkeljaar")
elif(jaar %4==0):
    print("Shrikkeljaar")
else:
    print("Geen shrikkeljaar")