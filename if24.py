a = int(input("Enter the First people age: "))
b = int(input("Enter the Second People age: "))
c = int(input("Enter the Third people age: "))
d = int(input("Enter the Fourth people age: "))
if a<b and a<c and a<d:
    print("The youngest one is",a)
elif b<a and a<c and b<d:
    print("The youngest one is",b)
elif c<d and c<a and c<b:
    print("The youngest one is",c)
else:
    print("The youngest one is",d)