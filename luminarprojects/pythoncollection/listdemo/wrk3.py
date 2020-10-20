lst=[1,2,3,4]
element=int(input("enter the no:"))
ln=len(lst)
for i in range(0,ln):
    for j in range(i,ln):
        if(lst[i]+lst[j]==element):
            print(lst[i],lst[j])









