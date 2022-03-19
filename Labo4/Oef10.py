
import random


def dobbelsteen():
    dobbel = random.randint(1,6)
    dobbel+= random.randint(1,6)
    return dobbel

worpen = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
for i in range(1000):
    werp = dobbelsteen()
    worpen[werp] = worpen[werp] + 1
expected = [2.78,5.56,8.33,11.11,13.89,16.67,13.89,11.11,8.33,5.56,2.78]
for key, value in worpen.items():
    print(f"{key}\t{'{:.2f}'.format(value/10)}\t{expected[key-2]}")