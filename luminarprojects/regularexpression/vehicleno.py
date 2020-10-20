f=open("testvehicle","r")
fout=open("validvehicle","w")
valid=[]
number=[]
for num in f:
    num=num.rstrip("\n")
    number.append(num)

import re
for num in number:
    rule="kl[\d]{2}[a-z]{1,2}[\d]{4}"
    match=re.fullmatch(rule,num)
    if match==None:
        pass
    else:
        valid.append(num)
for num in valid:
    fout.write(num+"\n")
