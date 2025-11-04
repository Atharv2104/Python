class Animal:
    def __init__(self,name):
          self.name=name

    def info(self):
         print("animal name:",self.name)


class dog(Animal):
     def sound(self):
          print(self.name,"barks")

d=dog("tommy")
d.info()
d.sound()