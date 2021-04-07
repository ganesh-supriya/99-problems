# check if num is prime or not
def prime(num):
    if (num==1):
         return False
    elif(num==2):
           return True
    else:
        for i in range(2,num):
              if( num % i == 0):
                 return False
        return True

print(prime(87))


