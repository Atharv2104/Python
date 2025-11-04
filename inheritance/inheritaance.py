class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class rectangle(shape):
        def __init__(self, x, y):
             super().__init__(x, y)

        def area(self):
             return self.x*self.y
r=rectangle(5,6)
print("area of rectangle:",r.area())