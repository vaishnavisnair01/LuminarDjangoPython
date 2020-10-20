f=open("dwnld","r")
dict={}
lst=[]
for lines in f:
    movies=lines.rstrip("\n").split(",")
    year=movies[2]

    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
for k,v in dict.items():
    print(k, ",", v)
    lst.append((v,k))
# print(lst)
srt=sorted(lst,reverse=True)
print(srt[0])



