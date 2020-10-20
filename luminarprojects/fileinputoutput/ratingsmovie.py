f=open("dwnld","r")
dict={}
rate=[]
for lines in f:
    words=lines.rstrip("\n").split(",")
    rating=words[3]
    # print(rating)
    if (rating != ''):
        if rating not in dict:
            dict[rating]=1
        else:
            dict[rating]+=1
for key,value in dict.items():
    # print(dict)
    rate.append((value,key))
    srt=sorted(rate,reverse=True)
print(srt)
print("Highest ratings",srt[0])
