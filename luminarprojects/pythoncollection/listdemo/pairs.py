lst=[1,2,3,4]
element=int(input("enter the no:"))
flag=0
low=0
total=0
upp=len(lst)-1
while(low<upp):
    total=lst[low]+lst[upp]
    if(total==element):
        flag+=1
        print("pairs are:",lst[low],lst[upp])
        break
    elif(total>element):
        upp-=1
    else:
        low+=1
if(flag==1):
    print("pairs are:",lst[low],lst[upp])
else:
    print("elements not found")