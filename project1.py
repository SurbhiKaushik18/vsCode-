import random
user_choice=int(input("Enter your choice: Type 0 for Rock, Type 1 for Paper and Type 2 for Scissor: "))
rock=""
paper=""
scissor=""
game_images=[rock,paper,scissor]
if user_choice>=3 or user_choice<0:
    print("You entered invalid number! You Lose.")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer choice: ", computer_choice)
    print(game_images[computer_choice])
    if user_choice==computer_choice:
        print("Draw")
    elif user_choice==2 and computer_choice==0:
        print("You lose")
    elif user_choice==0 and computer_choice==2:
        print("You win")
    elif user_choice>computer_choice:
        print("You Win")
    elif user_choice<computer_choice:
        print("You lose")
 