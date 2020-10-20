f=open("testmobileno","r")
number=[]
valid=[]
fout=open("validno.txt","w")
for no in f:
    no=no.rstrip("\n")
    number.append(no)

import re
rule="(91)?[\d]{10}"
for num in number:

    match=re.fullmatch(rule,num)
    if match==None:
        pass
    else:
        valid.append(num)
print(valid)
for num in valid:
    fout.write(str(num)+"\n")