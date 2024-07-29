a = input("Enter Student Name:- ")
b = int(input("Total number of working days:- "))
c = int(input("Total number of days for absent:-"))
d = (b-c)/b*100
print(d)
if d>=75:
    print(a,"is eligible for test exam.")
else:
    print(a,"is not eligible for test exam")