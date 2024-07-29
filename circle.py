class circle:
    def __init__(self,r):
        self.radius=r
        self.pi=22/7
    def area(self):
        area=self.pi*self.radius**2
        print(area)
    def peri(self):
        peri=2*self.pi*self.radius
        print(peri)

cir=circle(21)
print(cir.radius)
cir.area()
cir.peri()