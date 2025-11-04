#super keyword

class person:
     def __init__(self,name,age):
            self.name=name
            self.age=age
     def show(self):
            print("name:",self.name)
            print("age:",self.age)

class Student(person):
      def __init__(self, name, age):
            super().__init__(name,age)

      def show(self):
            super().show()


s=Student("Atharv",21)
s.show()





           