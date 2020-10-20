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
names=list(map(lambda obj:obj.name.upper(),lst))
print(names)
stud=list(filter(lambda obj:obj.total>450,lst))
for st in stud:
    print(st)
