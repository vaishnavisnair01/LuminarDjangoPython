lst=[1,3,5,7,9,24,10,3]
flag=0
elmt=int(input("enter the no:"))
for item in lst:
    if(item==elmt):
        flag+=1
        break
if(flag==1):
    print("element found")
else:
    print("element not found")

