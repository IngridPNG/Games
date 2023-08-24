#Rock = 0
#Paper = 1
#Scissors = 2

#The game
def game():
    choice = ["rock", "paper", "scissors"]
    print ("Rock, paper or scissors?")
    player_choice = input("Enter here: ").lower()
    import random
    computer_choice = random.randint(0,2)

    #If player chooses rock
    if computer_choice == 0 and player_choice == choice[0]:
        print ("Rock")
        print ("Tie")
    elif computer_choice == 1 and player_choice == choice[0]:
        print ("Paper")
        print ("You lose")
    elif computer_choice == 2 and player_choice == choice[0]:
        print ("Scissors")
        print ("You win!")

    #If player chooses paper
    elif computer_choice == 0 and player_choice == choice[1]:
        print ("Rock")
        print ("You win!")
    elif computer_choice == 1 and player_choice == choice[1]:
        print ("Paper")
        print("Tie")
    elif computer_choice == 2 and player_choice == choice[1]:
        print ("Scissors")
        print ("You lose")

    #If player chooses Scissors
    elif computer_choice == 0 and player_choice == choice[2]:
        print ("Rock")
        print ("You lose")
    elif computer_choice == 1 and player_choice == choice[2]:
        print ("Paper")
        print ("You win!")
    elif computer_choice == 2 and player_choice == choice[2]:
        print ("Scissors")
        print ("Tie")

    #Error message if player does anything else
    else:
        print ("Error")

    #Play again prompt
    print ("Play again?")
    playagain = input("Enter here: ").lower()
    if playagain == "yes":
        print ("Okay!")
        game()
    elif playagain == "no":
        print ("Okay!")
    else:
        print ("Error")
game()
