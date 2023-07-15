def game():
    import random

    print("Lets play Rock Paper and Scissors:")
    options=["rock","paper","scissors"]

    while True:
        user_input=input("Enter rock/paper/scissors:")
        if user_input not in options:
            continue
        random_number=random.randint(0,2)
        
        angel_pick=options[random_number]
        print("Angel picked:",angel_pick)
        
        if user_input=="rock"and angel_pick=="scissors":
            print("You won.")
            return "You win!!"
        
        elif user_input=="scissors" and angel_pick=="paper":
            print("You won.")
            return "You win!!"
        
        elif user_input=="paper" and angel_pick=="rock":
            print("You won.")
            return "You win!!"
        
        elif user_input==angel_pick:
            print("It's a draw the angel wants to play again.")
            continue
        
        else:
            print("Angel won.")
            return "You lost!!"
name=input("Enter your name:")
print("Hello",name,"Welcome to this adventure and you must guess correctly and believe in your guts to reach till the end!!")

answer=input("You are being chased by a tiger and there two ways.\ndecide where do you want to run(right/left):")

if answer=="right":
    answer=input("You have reached the end of the road and there is a river.\n Decide if you want to swim across it or go back(swim/back):")
    if answer=="back":
        print("You are eaten by the tiger you die!!!")
    elif answer=="swim":
        print("You are in river and eaten by an alligator")
    else:
        print("Invalid choice you die!!!")
    

elif answer=="left":
    answer=input("You haved entered in the forest and you are lost.\n Decide if you want to go back or keep going in the forest(back/keep going):")
    if answer=="back":
        print("You are eaten by tiger you die!!!")
    elif answer=="keep going":
        answer=input("You find a angel like figure.Do you to ask for help or keep going (help/keep going):")
        if answer=="keep going":
            print("You get lost and run out of food and you die!!!")
        elif answer=="help":
            print("The angel wants to play rock paper scissors if you win it will you show you the right direction.")
            result=game()
            if result=="You win!!":
                print("The angel has shown to you the way and you have won. Congratulations!!!")
            elif result=="You lost!!":
                print("The angel has got and it won't help and it disappears and you get lost and run out of food and you die!!!")
else:
    print("Invalid choice. You die!!!")
            
            
            
    
    
    
    
    
    

    
    
              
