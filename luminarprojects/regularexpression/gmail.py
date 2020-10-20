f=open("testgmail","r")
fout=open("validgmail","w")
gmail=[]
valid=[]
for id in f:
    id=id.rstrip("\n")
    gmail.append(id)

import re
rule="[a-z0-9.-_]{1,64}@gmail.com"

for id in gmail:
    match = re.fullmatch(rule, id)
    if match==None:
        pass
    else:
        valid.append(id)
for id in valid:
    fout.write(id+"\n")


