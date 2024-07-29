def cal_list(numbers):
    print(sum(numbers))
num=[2,3,4,4,5,6]   
cal_list(num)

def cal_lis(n):
    n.append(10)
    print(n)
num=[2,3,4,4]
cal_lis(num)

def cal_l(n):
    total=1
    for x in n:
        total=total*x
    print(total)
num=[2,3,-4,5]
cal_l(num)

def cal_rev(n):
    n.reverse()
    print(n)
num=['a','b','c','d']
cal_rev(num)

def cal_fact(n):
    x=1
    for i in range(1,n+1):
        x=x*i
    print(x)
cal_fact(4)




