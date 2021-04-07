#removing duplicates from list
list=['a','b','a','a','a','b','b','b','c','c','a','a','a','b','c','d']
print("the original list is :",list)
res=[]
for i in list:
    if i not in res:
        res.append(i)

print("list after removing duplicates :",res)
