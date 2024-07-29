a = int(input("Enter the percentage: "))
if a<25:
    print("Grade D")
elif a>=25 and a<45:
    print("Grade C")
elif a>=45 and a<50:
    print("Grade B")
elif a>=50 and a<60:
    print("Grade B+")
elif a>=60 and a<80:
    print("Grade A")
else:
    print("Grade A+")