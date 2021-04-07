
my_flatten=[('a',('b','c','d'),'e')]
list_flat = []
for i in range(len(my_flatten)):
    for j in range(len(my_flatten[i])):
        list_flat.append(my_flatten[i][j])

print("original list is:",my_flatten)
print("flatten list is :",list_flat)

'''import functools
import operator
my_flatten=[('a',('b',('c','d'),'e'))]
list_flat = functools.reduce(operator.iconcat,my_flatten,[])
print("original list is:",my_flatten)
print("flatten list is :",list_flat)
'''