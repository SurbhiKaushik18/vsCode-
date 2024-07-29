a = int(input("Enter the Percentage: "))

if a>90:
    print("Grade: A")
elif a>80 and a<=90:
    print("Grade: B")
elif a>=60 and a<80:
    print("Grade: C")
else:
    print("Grade: D")