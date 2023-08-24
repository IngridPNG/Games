correct_guesses = ["S", "L", "A", "T", "E"]
incorrect_guesses = ["B", "C", "D", "F", "G", "H", "I", "J", "K", "M", "N", "O", "P", "Q", "R", "U", "V", "W", "X", "Y", "Z"]
word = ["_", " _", " _", " _", " _"]
wrong_guess_limit = 6

def game(wrong_guess_count = 0):
    global word
    
    if wrong_guess_count == 0:
        
        print ("  _______     ")
        print ("  |    |      ")
        print ("  |    |      ")      
        print ("  |           ")     
        print ("  |           ")
        print ("  |           ")                
        print ("  |           ")
        print (" _|_          ")   
        print ("|   |______   ")
        print ("|          |  ")
        print ("|__________|  ")
        print ("              ")
        print (*word           )
        print ("              ")
        print ("" + str(wrong_guess_count) + "/6 wrong guesses")
        print ("Only letter guesses are allowed")

               
    elif wrong_guess_count == 1:
               
        print ("  _______     ")
        print ("  |    |      ")
        print ("  |    |      ")      
        print ("  |    o      ")     
        print ("  |           ")
        print ("  |           ")                
        print ("  |           ")
        print (" _|_          ")   
        print ("|   |______   ")
        print ("|          |  ")
        print ("|__________|  ")
        print ("              ")
        print (*word           )
        print ("              ")            
        print ("" + str(wrong_guess_count) + "/6 wrong guesses")
        print ("Only letter guesses are allowed")
        
    elif wrong_guess_count == 2:

        print ("  _______     ")
        print ("  |    |      ")
        print ("  |    |      ")      
        print ("  |    o      ")     
        print ("  |    |      ")
        print ("  |    |      ")                
        print ("  |           ")
        print (" _|_          ")   
        print ("|   |______   ")
        print ("|          |  ")
        print ("|__________|  ")
        print ("              ")
        print (*word           )
        print ("              ")
        print ("" + str(wrong_guess_count) + "/6 wrong guesses")
        print ("Only letter guesses are allowed")
        
    elif wrong_guess_count == 3:

        print ("  _______     ")
        print ("  |    |      ")
        print ("  |    |      ")      
        print ("  |    o      ")     
        print ("  |    |\     ")
        print ("  |    |      ")                
        print ("  |           ")
        print (" _|_          ")   
        print ("|   |______   ")
        print ("|          |  ")
        print ("|__________|  ")
        print ("              ")
        print (*word           )
        print ("              ")
        print ("" + str(wrong_guess_count) + "/6 wrong guesses")
        print ("Only letter guesses are allowed")
        
    elif wrong_guess_count == 4:

        print ("  _______     ")
        print ("  |    |      ")
        print ("  |    |      ")      
        print ("  |    o      ")     
        print ("  |   /|\     ")
        print ("  |    |      ")                
        print ("  |           ")
        print (" _|_          ")   
        print ("|   |______   ")
        print ("|          |  ")
        print ("|__________|  ")
        print ("              ")
        print (*word           )
        print ("              ")
        print ("" + str(wrong_guess_count) + "/6 wrong guesses")
        print ("Only letter guesses are allowed")
        
    elif wrong_guess_count == 5:
  
        print ("  _______     ")
        print ("  |    |      ")
        print ("  |    |      ")      
        print ("  |    o      ")     
        print ("  |   /|\     ")
        print ("  |    |      ")                
        print ("  |   /       ")
        print (" _|_          ")   
        print ("|   |______   ")
        print ("|          |  ")
        print ("|__________|  ")
        print ("              ")
        print (*word           )
        print ("              ")
        print ("" + str(wrong_guess_count) + "/6 wrong guesses")
        print ("Only letter guesses are allowed")
        
    elif wrong_guess_count == 6:
  
        print ("  _______     ")
        print ("  |    |      ")
        print ("  |    |      ")      
        print ("  |    o      ")     
        print ("  |   /|\     ")
        print ("  |    |      ")                
        print ("  |   / \     ")
        print (" _|_          ")   
        print ("|   |______   ")
        print ("|          |  ")
        print ("|__________|  ")
        print ("              ")
        print (*word           )
        print ("              ")
        print ("" + str(wrong_guess_count) + "/6 wrong guesses")
        print ("You lose")
        guess = "  "
        print ("Try again?")
        tryagain = input ("Enter here: ").lower()
        if tryagain == "yes":
            wrong_guess_count = 0
            word = ["_", " _", " _", " _", " _"]
            game(wrong_guess_count)
        elif tryagain == "no":
            print ("Okay!")

    if word == ["S", "L", "A", "T", "E"]:
        print ("You win!")
        print ("Play again?")
        tryagain = input ("Enter here: ").lower()
        if tryagain == "yes":
            wrong_guess_count = 0
            word = ["_", " _", " _", " _", " _"]
            game(wrong_guess_count)
        if tryagain == "no":
            print ("Okay!")
            return
        
    if wrong_guess_count < wrong_guess_limit and word != ["S", "L", "A", "T", "E"]: 
        guess = input ("Enter guess here: ").upper()

    if guess[0] == (correct_guesses)[0] and "S" not in word:
        word[0] = "S"
        print ("There is an " + (guess) + " in the word!")
        game(wrong_guess_count)
    elif guess[0] == (correct_guesses)[1] and "L" not in word:
        word[1] = "L"
        print ("There is an " + (guess) + " in the word!")
        game(wrong_guess_count)
    elif guess[0] == (correct_guesses)[2] and "A" not in word:
        word[2] = "A"
        print ("There is an " + (guess) + " in the word!")
        game(wrong_guess_count)
    elif guess[0] == (correct_guesses)[3] and "T" not in word:
        word[3] = "T"
        print ("There is a " + (guess) + " in the word!")
        game(wrong_guess_count)
    elif guess[0] == (correct_guesses)[4] and "E" not in word:
        word[4] = "E"
        print ("There is an " + (guess) + " in the word!")
        game(wrong_guess_count)
    elif guess[0] in word:
        print ("You have already guessed " + (guess[0]) + "!")
        game(wrong_guess_count)
    elif guess[0] in incorrect_guesses:
        print ("There is no " + (guess) + " in the word")
        wrong_guess_count += 1
        game(wrong_guess_count)
    elif guess[0] not in correct_guesses or incorrect_guesses:
        print ("Only letter guesses are allowed!")
        game(wrong_guess_count)
    else:
        print ("Error")

game()
 
