class person:
    def __init__(self,name):
        self.name=name

class employee(person):
     def role(self):
         print(self.name,"is a employee")

e=employee("om")
print("name:",e.name)
e.role()
