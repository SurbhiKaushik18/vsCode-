def fabonacci(num):
    if num==0:
        return 0
    elif (num==1 or num==2):
        return 1
    else:
        return(fabonacci(num-1)+fabonacci(num-2))
print(fabonacci(8))