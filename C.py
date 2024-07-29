for row in range(6):
    for col in range(8):
        if (col==0 and (row>1 and row<4)) or (col==1 and (row==1 or row==4)) or (row==0 and col>1 or row==5 and col>1):
            print("*",end=" ")
        else:
            print(end=" ")
    print()