input = input("Geef een string : ")
IsPalindroom = True
for i in range(len(input)):
    if(input[i] != input[len(input)-i-1]):
        IsPalindroom = False
print(IsPalindroom)