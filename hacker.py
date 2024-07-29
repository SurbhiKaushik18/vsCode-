n=[i for i in range(1,100) if i%7==0]
print(n)

n1=[i for i in range(1,10) if '3' in str(i)]
print(n1)

a='surbhi'
n2=[i for i in a if i=='']
print(len(n2))

l=[1,2,3,4,5,6]
print(l)
m=l.copy()
m[0]=0
print(l)
print(m)