num=int(input("enter the number"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=0
        break
    else:
        flag=1
if(flag==1):
    print("number is prime")
else:
    print("number is not prime")

