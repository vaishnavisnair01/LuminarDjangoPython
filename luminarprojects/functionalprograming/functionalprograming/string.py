text="HHHPPSDAA"
cnt=0
ntext={}
res=""
for i in text:
    if i in ntext:
        ntext[i]+=1

    else:
        ntext[i]=1
print(ntext)

for k,v in ntext.items():
    res+=str(v)+k
print(res)




