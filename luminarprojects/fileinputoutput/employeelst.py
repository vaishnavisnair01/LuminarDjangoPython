ref=open("employee","r")
eid=[]
ename=[]
esalary=[]
for lines in ref:
    line=lines.rstrip("\n")
    words=line.split(",")
    id=words[0]
    name=words[1]
    sal=words[2]
    ename.append(name)
    esalary.append(sal)
    eid.append(id)
print(eid)
print(ename)
print(esalary)
