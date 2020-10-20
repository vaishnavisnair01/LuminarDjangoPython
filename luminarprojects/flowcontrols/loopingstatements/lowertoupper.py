lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
i=lower
if(lower<=upper):
    while(i<upper):
        print(i)
        i=i+1
else:
    print("invalid input")
