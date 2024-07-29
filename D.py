for row in range(8):
    for col in range(5):
        if (col==0 and ( row>0 and row<7)) or (row==0 and  (col>0 and col<3)):
            print("*",end="")
        else:
            print(end="")
    print()
 