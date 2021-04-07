# greatest common divisior
#recursion method
def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

print(gcd(36,63))

