import random
a=int(input("User_Choice: "))
b=random.randint(0,109)
print("Computer_Choice:",b)
c=input("Task_Performed: ")
if c=="addition":
    print("Sum =",a+b)
elif c=="Subtraction":
    print("subtraction =",a-b)
else:
    print("No result")