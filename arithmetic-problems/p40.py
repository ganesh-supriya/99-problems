#goldbach's conjecture

def iseven(num):
    if num % 2==0:
        return True
    else:
        return False
def isprime(num):
    if num==0 or num==1:
        flag=False
    elif num==2:
        flag=True
    else:
        for i in range(2,num):
            if num % i ==0:
                flag=False
                break
            else:
                flag= True
    return flag

number = int(input("please enter a number"))
if  iseven(number):
    list=[]
    print(list)
    for i in range(1,number):
        j=number-i

        if isprime(i) and isprime(j):
            list.append(i)
            if j in list:
                pass
            else:

               print('{0}={1}+{2}'.format(number,i,j))



