logo = '''
 _                 _______  ______   _______  _______    _______           _______  _______  _______ _________ _        _______    _______  _______  _______  _______ 
( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )  (  ____ \|\     /|(  ____ \(  ____ \(  ____ ||__   __/( (    /|(  ____ \  (  ____ \(  ___  )(       )(  ____ |
|  \  ( || )   ( || () () || (   ) )| (    \/| (    )|  | (    \/| )   ( || (    \/| (    \/| (    \/   ) (   |  \  ( || (    \/  | (    \/| (   ) || () () || (    \/
|   \ | || |   | || || || || (__/ / | (__    | (____)|  | |      | |   | || (__    | (_____ | (_____    | |   |   \ | || |        | |      | (___) || || || || (__    
| (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)  | | ____ | |   | ||  __)   (_____  )(_____  )   | |   | (\ \) || | ____   | | ____ |  ___  || |(_)| ||  __)   
| | \   || |   | || |   | || (  \ \ | (      | (\ (     | | \_  )| |   | || (            ) |      ) |   | |   | | \   || | \_  )  | | \_  )| (   ) || |   | || (      
| )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__  | (___) || (___) || (____/\/\____) |/\____) |___) (___| )  \  || (___) |  | (___) || )   ( || )   ( || (____/|
|/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/  (_______)(_______)(_______/\_______)\_______)\_______/|/    )_)(_______)  (_______)|/     \||/     \|(_______/
                                                                                                                                                                      
'''
from random import randrange
print(logo)
print("Welcome to number guessing game!\nI will guess number between 1 to 100.")
continue_play = True
guessednumber = randrange(1,101)
print(f"psst, the guessed number is {guessednumber}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': (easy) ")
if difficulty == 'hard':
    lives = 5
else:
    lives = 10
while lives:
    print(f"You have {lives} attempts remaining to guess the number.")
    userguess = int(input("Make a guess : "))

    if (userguess > 0) and (userguess < 101):
        if userguess == guessednumber:
            print("Awesome,you guessed it right.")
            lives = 0
            continue
        if userguess > guessednumber:
            print("too high")
        else:
            print("too low")
        lives -= 1
        if (lives == 0):
            print("You've run out of guesses, you lose.")
            continue
    else:
        print("Wrong input, try again, valid input is '1' to '100'.")