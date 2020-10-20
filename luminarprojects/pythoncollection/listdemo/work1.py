lst=[1,2,3,5]
nlst=[]
count=0
for item in lst:
    count+=1
    nlst.append(item**count)
print(nlst)