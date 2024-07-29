n=int(input("Enter the number: "))
fac=1
for i in range(1,n+1):
    fac=fac*i
print("factorial is", fac)

def fact_num(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
fact_num(7)