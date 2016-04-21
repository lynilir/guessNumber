print "Please think of a number between 0 and 100!"

high = 100
low = 0
numGuess = 0

x = (low+high)/2
while True:

    print "Is your secret number " + str(x) + "?"
    userInput = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if userInput == "l":
        low = x
        x = (low+high)/2
    elif userInput == "h":
        high = x
        x = (low+high)/2
    elif userInput == "c":
        print "Game over. Your secret number was: " + str(x)
        break
    else:
        print "Sorry, I did not understand your input."
        
