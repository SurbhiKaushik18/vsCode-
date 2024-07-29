class Employee:
    color="black"
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showdetails(self):
        print("Role:",self.role)
        print("Department:",self.department)
        print("Salary:",self.salary)
    def start(self):
        print("car start")
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
   

emp1=Employee("Professor","Cs","23456")
emp1.showdetails()
emp2=Engineer("Surbhi","34")
emp2.start()


