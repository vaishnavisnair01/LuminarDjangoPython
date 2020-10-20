class Employee:
    def __init__(self,id,name,salary,exp,desig):
        self.id=id
        self.name=name
        self.salary=salary
        self.exp=exp
        self.desig=desig
    def setEmployee(self):
        print("id=",self.id)
        print("name=",self.name)
        print("salary=",self.salary)
        print("experience=",self.exp)
        print("designation=",self.desig)
    def __str__(self):
        return self.name


f=open("employee","r")
emp=[]
for data in f:
    data=data.rstrip("\n").split(",")
    id=data[0]
    name=data[1]
    salary=int(data[2])
    exp=data[3]
    desig=data[4]
    obj=Employee(id,name,salary,exp,desig)
    emp.append(obj)


desig=[obj.name for obj in emp if obj.desig=="developer"]
print(desig)
upp=[obj.name.upper() for obj in emp]
print(upp)
tot=sum([obj.salary for obj in emp])
print(tot)
high=max([obj.salary for obj in emp])
print(high)