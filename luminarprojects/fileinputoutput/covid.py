f=open("data2","r")
fout=open("covidut.txt","w")
covid=[]
dict={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    state=words[1]
    cases=float(words[4])
    # print(state,cases)
    # break
    if state not in dict:
        dict[state]=cases
    else:
        dict[state]=cases
# print(dict)
for k,v in dict.items():
    covid.append((v,k))
    lst=sorted(covid,reverse=True)
print(lst[0])
for val in lst:
    fout.write(str(val)+"\n")



