# rotate list to nth places
list=[1,3,2,4,5,2,6,7]

length = len(list)
print(list)
print(length)
print("rotate a list from index 3:")
list=list[3:] + list[:3]
print (list)

