#pack duplicates of list in sublist
from itertools import groupby
def pack_duplicates(l_nums):
    return [list(group) for key,group in groupby(l_nums)]
list1=[0,0,1,1,2,2,3,3,6,8,8,9,9,9]
print("original list:",list)
print("after packing consecutive duplicates in sublist:")
print(pack_duplicates(list1))


#error
