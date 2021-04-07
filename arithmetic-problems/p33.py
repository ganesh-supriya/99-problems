
#coprime
def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
def coprime(x,y):
    return gcd(x,y)==1

print(coprime(35,64))

