a = int(input("Enter the units: "))
if a<=100:
    print("No charge")
elif a>100 and a<=200:
    print("The price is:" , (a-100)*5 )
else :
    print("The price is:", (a-200)*10+500)