#euler's totient formula 2

def eular(n):
    result=n
    p=2
    while p* p<= n:
        if n % p == 0:        #check if p is prime factor
            while n % p == 0:    #if yes update n and result
                n= n//p
            result = result *(1-(1/float(p)))
        p=p+1

    if n>1:
        result=result*(1-(1/float(p)))
    return int(result)


for n in range(1,11):
    print("phi(",n,"):",eular(n))
