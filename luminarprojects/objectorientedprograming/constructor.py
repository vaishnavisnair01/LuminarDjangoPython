class Employee:
    company_name="luminar"
    def __init__(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printEmp(self):
        print("id",self.id)
        print("desg",self.desig)
        print("company name",Employee.company_name)
        print("salary",self.salary)
emp=Employee(101,"dev",3000)
emp.printEmp()
