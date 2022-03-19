def listFromat(list:list):
    out = ""
    for i in list[:-2]:
        out +=(f"{i}, ")
    out+=f"{list[-2]} en "
    out+=f"{list[-1]}"
    return out
print(listFromat([1,3,4,5]))