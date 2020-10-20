lst=[2,3,5]
nlst=[]
sum=0
new=0
for i in lst:
    sum+=i
print(sum)
for i in lst:
    new=sum-i
    nlst.append(new)
print(nlst)

