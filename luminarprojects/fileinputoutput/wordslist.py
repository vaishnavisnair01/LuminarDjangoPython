ref=open("news","r")
lst=[]
for lines in ref:
    line=lines.rstrip("\n")
    word=line.split(" ")
    for i in word:
        lst.append(i)
print(lst)