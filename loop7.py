n=int(input("Enter the number: "))
for i in range(0,n+2):
    for j in range(0,n-i-1):
        print(end="")
    for j in range(0,i+1):
        print("*",end="")
    print()