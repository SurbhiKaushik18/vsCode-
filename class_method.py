class surbhi:
    name="Surbhi"
    def sur(self,age):
        self.age=age
        print(age)
    @classmethod
    def ChangeName(cls,name):
        cls.name=name
p1=surbhi()
p1.ChangeName("Bhavya")
print(p1.name)
p1.sur("12")


