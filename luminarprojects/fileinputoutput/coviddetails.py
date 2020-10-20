f=open("data2","r")
covid={}
for data in f:
    data=data.rstrip("\n").split(",")
    states=data[1]
    confirmed=data[4]
    deadth=data[5]
    cured=data[6]
    if states not in covid:
        covid[states]={"state":states,"confirmed":confirmed,"deadth":deadth,"cured":cured}
    else:
        pass
for k,v in covid.items():
    print(k,"-->",v)
def getDetails(**args):
    state=args["states"]
    prope=args["prop"]
    print("cured people is",state,covid[state][prope])



getDetails(states="Kerala",prop="cured")