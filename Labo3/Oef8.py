def priem(getal):
    for i in range(2,getal):
        if(getal % i == 0):
            return False
    return True

print(priem(11))