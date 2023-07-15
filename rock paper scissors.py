import random

print("Lets play Rock Paper and Scissors:")
options=["rock","paper","scissors"]

while True:
    user_input=input("Enter rock/paper/scissors:")
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    
    computer_pick=options[random_number]
    print("Computer picked:",computer_pick)
    
    if user_input=="rock"and computer_pick=="scissors":
        print("You wins!!")
        break
    
    elif user_input=="scissors" and computer_pick=="paper":
        print("You win!!")
        break
    
    elif user_input=="paper" and computer_pick=="rock":
        print("You win!!")
        break
    
    elif user_input==computer_pick:
        print("Draw")
        break
    
    else:
        print("You lost!!")
        break
    