class person:
    def __init__(self,name):
        self.name=name

class Job:
    def __init__(self,salary):
        self.salary=salary

class employee(person,Job):
    def __init__(self, name,salary):
        person.__init__(self,name)
        Job.__init__(self,salary)   

    def details(self):
        print(self.name,"is a employee with salary",self.salary)
e=employee("om",50000) 
print("name:",e.name) 
print("salary:",e.salary)
e.details()          
        

