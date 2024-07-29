a = int(input("Years of Service:"))
b = int(input("Salary: "))
if a>10:
    b = (b*10)/100
    print(b)
elif a>=6 and a<=10:
    b = (b*8)/100
    print(b)
else:
    b = (b*5)/100
    print(b)

