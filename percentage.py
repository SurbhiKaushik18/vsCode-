class student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        
    @property 
    def cal(self):
        return str((self.phy+self.chem+self.maths)/3)
        
        
s1=student(98,97,99)
print(s1.cal)

s1.phy=4
print(s1.cal)