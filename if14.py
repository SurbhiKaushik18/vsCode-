"""a = int(input("Enter the no. : "))
if a>=100 and a<=999:
    print("Entered Value is Three digit Number.")
else:
    print("Entered value is not three digit number.")

num1=input("Enter any Number.")
l=len(num1)
if l!=3:
    print("Enter three digit number")
else:
    print("Middle digit is",(int(num1)%100//10))"""

a = input("Enter the number: ")
if len(a)==3:
    print("Entered NUmber is three digit number.")
else:
    print("Entered number is not three digit number.")