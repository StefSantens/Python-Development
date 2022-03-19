def anagram(string1,string2):
    dict1 = {}
    dict2 = {}
    for i in string1:
        dict1[i.lower()] = "aanwezig"
    for i in string2:
        dict2[i.lower()] = "aanwezig"
    return dict1 == dict2

print(anagram("Marten Asmodom Vilijn","Mijn naam is Voldemort"))