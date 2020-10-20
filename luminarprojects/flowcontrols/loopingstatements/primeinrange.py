low=int(input("enter the lower limit:"))
upper=int(input("enter the upper limit:"))
flag=0
for i in range(low,upper):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                flag=0
        else:
            print(i)
