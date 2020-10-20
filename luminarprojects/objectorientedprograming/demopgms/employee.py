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
salary=[]
for obj in emp:
    # print(obj)
    salary.append(obj.salary)
maxi=max(salary)
if(maxi==obj.salary):
    print("max salary employee:",obj)

from functools import *
for obj in emp:
    designation=list(filter(lambda obj:obj.desig=="developer",emp))
for des in designation:
    print(des)
    upper=list(map(lambda obj:obj.name.upper(),emp))
print(upper)
for obj in emp:
    high=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,list(map(lambda obj:obj.salary,emp)))
    totsal=reduce(lambda sal1,sal2:sal1+sal2,list(map(lambda obj:obj.salary,emp)))
print(high)
print(totsal)

