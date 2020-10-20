ar=[2,3,7,8,5]
ar.sort()
print(ar)
low=0
upp=0
flag=0
element=int(input("enter the no to search:"))
upp=len(ar)

while(low<=upp):
    mid=(low+upp)//2
    if(element>ar[mid]):
        low=mid+1
    elif(element<ar[mid]):
        upp=mid-1
    elif(element==ar[mid]):
        flag=1
        break
if(flag==1):
    print("element found",mid)
else:
    print("element not found")

