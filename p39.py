#list of all prime no within range

start= int(input("enter starting no"))
end = int(input("enter last no"))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
           if(num%i)==0:
                  break
        else:
          print(num)
