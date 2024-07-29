a=input("Are you ready for the KBC: ")
if a=='Yes':
    print("Lets Start.")
else:
    print("OK, All the best for your future.")


q=['1. who is the President of India?','2. Who is the Prime Minister of India?']
for i in q:
    print(i)
    b=input("Your Answer: ")
    if q[0]=="Draupadi murmur":
        print("win")
    else:
        print("You lose")
