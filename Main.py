print ("What game would you like to play?")
print ("Game options are Rock paper scissors (RPS) and hangman")
gamechoice = input ("Enter here: ").lower()
if gamechoice == "hangman":
    import Hangman
if gamechoice == "rock paper scissors" or gamechoice == "rps":
    import Rock_Paper_Scissors
