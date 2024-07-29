a = int(input("Enter the cost price of a bike: "))

if a>100000:
    a=15/100*a
    print("You have to pay tax of: ",a )
elif a>50000 and a<=100000:
    a=10/100*a
    print("You have to pay tax of:",a)
elif a<=50000:
    a=5/100*a
    print("You have to pay tax of:",a)