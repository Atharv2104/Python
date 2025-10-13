#metod overriding
class person:
        def __init__(self,name,age):
                self.name=name
                self.age=age
        def show(self):
                print("name:",self.name)
                print("age:",self.age)
class Employee(person):
        
    def __init__(self, name, age, salary):
        
        super().__init__(name, age)
        self.salary = salary

    
    def show(self):
        
        super().show()
        print("salary:", self.salary)

E = Employee("Atharv", 21, 50000)
E.show()
        












                    