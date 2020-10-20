class Person:
    def setValue(self,ag,nam):
        self.age=ag
        self.name=nam

    def printValues(self):
        print("age=",self.age)
        print("name=",self.name)

obj=Person()
obj.setValue(27,"ajay")
obj.printValues()
