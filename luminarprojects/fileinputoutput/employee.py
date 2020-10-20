f=open("employee","r")
employee={}
lst=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    # print(data)
    id=data[0]
    name=data[1]
    sal=data[2]
    exp=data[3]
    des=data[4]
    if id not in employee:
        employee[id]={"id":id,"name":name,"salary":sal,"exp":exp,"design":des}
for k,v in employee.items():
    print(k,"->",v)
def employeedetails(**args):
    eid=args["id"]
    prope=args["prop"]
    print(employee[eid]["name"])
    print(employee[eid][prope])



employeedetails(id='1001',prop='exp')