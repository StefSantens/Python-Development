def anagram(string1,string2):
    dict1 = {}
    dict2 = {}
    for i in string1:
        dict1[i] = "aanwezig"
    for i in string2:
        dict2[i] = "aanwezig"
    return dict1 == dict2

print(anagram("datzalwel","welzaldat"))