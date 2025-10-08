class person:
    def __init__(self,name):
        self.name=name

class employee(person):
    def role(self): 
        print(self.name,"is a employee")  

class manager(employee):
    def department(self,dept):
        print(self.name,"is a manager of",dept,"department")

m=manager("om")
print("name:",m.name)
m.role()
m.department("IT")

        