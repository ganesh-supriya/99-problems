#replicate the element in list
list = ['a','b','c','d']
print("the original list is:",list)

k=3
res = [ele for ele in list for i in range(k)]

print(res)

