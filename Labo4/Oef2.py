def dellist(list:list,getal:int):
    if(len(list) <= getal*2):
        return "fout"
    else:
        list.sort()
        list = list[getal:-getal]
        return list

print(dellist([4,6,7,3,2,1,9,8,5],3))