a = int(input("Enter first sides:"))
b = int(input("Enter second sides:"))
c = int(input("Enter third sides:"))
if a==b and b==c:
    print("Equilateral Triangle.")
elif a!=b and b!=c and c!=a:
    print("Scalen Triangle.")
else:
    print("Isosceles Trianle.")

