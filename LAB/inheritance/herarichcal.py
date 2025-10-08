class person:
    def __init__(self,name):
        self.name=name

class employee(person):
    def role(self):
        print(self.name,"is a employee")

class intern(person):
     def role(self):
         print(self.name,"is a intern")

e=employee("om")
print("name:",e.name)
e.role()
i=intern("ram")
print("name:",i.name)   
i.role()
        