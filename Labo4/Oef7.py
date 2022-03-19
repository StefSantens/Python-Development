def is_sublist(lst1, lst2):
   ls1 = [element for element in lst1 if element in lst2]
   return ls1 == lst2

print(is_sublist([1,2,3],[1,2,3,4]))