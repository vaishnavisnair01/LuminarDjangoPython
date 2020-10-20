text="ABABCCC"
dict={}
for i in text:
    if(i not in dict):
        dict[i]=1
    else:
        print(i,"is the recursive chara")
        break
