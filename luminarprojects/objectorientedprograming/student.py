class Student:
    def setStudent(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total
    def printStudents(self):
        print(self.rol)
        print(self.name)
        print(self.course)
        print(self.total)
obj=Student()
obj.setStudent(1,"appu","cse",100)
obj.printStudents()
