ref=open("random","r")
lst=[]
for lines in ref:
    line=lines.rstrip("\n")
    words=line.split(" ")
    for i in words:
        word=i.upper()
        lst.append(word)
print(lst)
