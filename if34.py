a = int(input("Enter the age:"))
b = input("Enter Gender:")
c = int(input("No. Of Days:"))
if a>=18 and a<30:
    if b=='f':
        print("No. of wages", c*750)
    else:
        print("No. of Wages",c*700)
elif a>=30 and a<=40:
    if b=='f':
        print("No. of Wages",c*850)
    else:
        print("No. of Wages", c*800)
else:
    print("Enter appropriate age")