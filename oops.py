class Surbhi:
    carrer="S.E"
    love="PMSVB"
bhavya=Surbhi()
print(bhavya.carrer)
print(bhavya.love)

class Surbhi:
    def __init__(self,fullname):
        self.name=fullname
        print("Adding new name in database: ")
s1=Surbhi("Bhavya")
print(s1.name)

class Family:
    college_name="abc"
    def __init__(self,fullname):
        self.nam=fullname
        print("Show the name of your family member: ")
s2=Family("PMVSB")
print(s2.nam)

s3=Surbhi("Silki")
print(s3.name)
print(s2.college_name)
