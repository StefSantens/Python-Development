def omgekeerd_zoeken(dict:dict,waarde):
    list = []
    for key,value in dict.items():
        if(value == waarde):
            list.append(key)
    return list

print(omgekeerd_zoeken({"test":"123","werkt":"123","zijde zeker":"nee"},"123"))