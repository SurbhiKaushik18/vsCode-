"""class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        return self.marks
s1=student("Vishal",2)
print(s1.name,s1.marks)
s2=student("Silki",2)
print(s2.name,s2.marks)
s3=student("Surbhi",2)
print(s3.name,s3.marks)
print("average",(s1.avg()+s2.avg()+s3.avg())/3)"""

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        return sum(self.marks)/3
s1=student("Surbhi",[3,3,3])
print(s1.name,s1.marks)
print("Average",s1.avg())
