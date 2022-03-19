import random
def lotto():
    out = []
    out2 = {}
    while(len(out2) < 6):
        x = random.randint(1,10)
        out.append(x)
        out2 = set(out)
    return out2
for i in lotto():
    print(i)