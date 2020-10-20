class Student:

    def __init__(self,roll,name,course,total):
        self.roll=roll
        self.name=name
        self.course=course
        self.total=total

    def printStudent(self):
        print(self.roll)
        print(self.name)
        print(self.course)
        print(self.total)
    def __str__(self):
        return self.name


f=open("student","r")
lst=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    # print(data)
    id=data[0]
    name=data[1]
    course=data[2]
    total=int(data[3])
    obj=Student(id,name,course,total)
    lst.append(obj)

totlst=[]
for obj in lst:
    # print(obj)
    if(obj.total>450):
        print(obj)
    totlst.append(obj.total)
# print(totlst)
maxt=max(totlst)
print(maxt)
for obj in lst:
    if(maxt==obj.total):
        print("max marks",(obj))








