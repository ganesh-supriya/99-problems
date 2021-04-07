#find last element of list

list = ['a','b','c','d']
print("the original list :",str(list))

for i in range(0, len(list)):
    if i == (len(list)-1):
        print("the last element of list is :",str(list[i]))

