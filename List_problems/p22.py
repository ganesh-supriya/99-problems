#creating list within given range
'''
import random
def range1(start,end,numbers):
    my_list=[]
    for i in range(numbers):
        my_list.append(random.randint(start,end))

        return my_list
numbers = 10
start = 1
end = 10

print(range1(start,end,numbers))
'''

my_list =[]
start=4
end=9
if start<end:
    my_list.extend(range(start,end))
    my_list.append(end)

print(my_list)

#error