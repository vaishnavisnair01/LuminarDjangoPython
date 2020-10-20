class Student:
    collagename="luminar"
    def __init__(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self.marks=marks
    def printStudent(self):
        print("roll",self.roll)
        print("class",self.name)
        print("college",Student.collagename)
        print("marks",self.marks)
    def __str__(self):
        return self.name
obj=Student(1,"ajay",100)
obj.printStudent()
obj1=Student(1002,"vinay",150)
print(obj)
print(obj1)