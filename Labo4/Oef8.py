from Oef7 import is_sublist

def all_sublists(list):
    lists = []
    for x in range(len(list)+1):
        for y in range(len(list)+1):
            if(is_sublist(list,list[x:y])):
                if(list[x:y] not in lists):
                    lists.append(list[x:y])
    return lists

print(all_sublists([1,2,3,4]))