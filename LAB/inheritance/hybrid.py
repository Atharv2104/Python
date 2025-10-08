class person:
    def __init__(self, name):

        self.name = name
class employee(person):
    def role(self):
        print(self.name, "is a employee")

class project:
    def __init__(self,Projectname):
        self.Projectname=Projectname

class Teamlead(employee,project):
    def __init__(self, name,Projectname):
        person.__init__(self, name)
        project.__init__(self,Projectname)
    def details(self):
        print(self.name, "is a Teamlead of project",self.Projectname)

lead=Teamlead("om","AI")
print("name:", lead.name)
print("Projectname:", lead.Projectname)
lead.role()
lead.details()

        

    
        