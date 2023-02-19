"""
THIS IS THE TRADDITIONAL ROCK PAPER SCISSORS LIZARD SPOCK

As Sheldon explains, \"Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.\"

"""

import random

#DEfine the option set
option_set = ('scissor', 'rock', 'paper', 'lizard', 'spock')

#MEssages
print("***"*10)
print('Remember the rules: \n\n\"Scissors cuts paper, \npaper covers rock, \nrock crushes lizard, \nlizard poisons Spock, \nSpock smashes scissors, \nscissors decapitates lizard, \nlizard eats paper, \npaper disproves Spock, \nSpock vaporizes rock, \nand as it always has, rock crushes scissors.\"\n')
print("***"*10)

#VAlidate user input
user_option = input(f"\nchose an option:{option_set}: ").lower()
while user_option not in option_set:
    print("Wrong selection, pick again!!")
    user_option = input(f"\nchose an option:{option_set}: ").lower()

user_wins = 0
computer_wins = 0

continue_playing = True
while continue_playing:
    #define the compute random selection
    computer_option = random.choice(option_set)

    #If statement
    if user_option == computer_option:
        print(f"user option was: {user_option}, and computer option was: {computer_option}")
        print("nobody Wins!!")
    elif user_option == 'scissor':
        if computer_option == 'paper' or computer_option == 'lizard':
            print(f"user option was: {user_option}, and computer option was: {computer_option}")
            user_wins += 1
            print("User Wins!!")
        elif computer_option == 'spock' or computer_option == 'rock':
            print(f"user option was: {user_option}, and computer option was: {computer_option}")
            computer_wins += 1
            print("Computer Wins!!")
    elif user_option == 'paper':
        if computer_option == 'rock' or computer_option == 'spock':
            print(f"user option was: {user_option}, and computer option was: {computer_option}")
            user_wins += 1
            print("User Wins!!")
        elif computer_option == 'lizard' or computer_option == 'scissor':
            print(f"user option was: {user_option}, and computer option was: {computer_option}")
            computer_wins += 1
            print("Computer Wins!!")
    elif user_option == 'rock':
        if computer_option == 'lizard' or computer_option == 'scissor':
            print(f"user option was: {user_option}, and computer option was: {computer_option}")
            user_wins += 1
            print("User Wins!!")
        elif computer_option == 'spock' or computer_option == 'paper':
            print(f"user option was: {user_option}, and computer option was: {computer_option}")
            computer_wins += 1
            print("Computer Wins!!")
    elif user_option == 'lizard':
        if computer_option == 'spock' or computer_option == 'paper':
            print(f"user option was: {user_option}, and computer option was: {computer_option}")
            user_wins += 1
            print("User Wins!!")
        elif computer_option == 'rock' or computer_option == 'scissor':
            print(f"user option was: {user_option}, and computer option was: {computer_option}")
            computer_wins += 1
            print("Computer Wins!!")
    elif user_option == 'spock':
        if computer_option == 'scissor' or computer_option == 'rock':
            print(f"user option was: {user_option}, and computer option was: {computer_option}")
            user_wins += 1
            print("User Wins!!")
        elif computer_option == 'paper' or computer_option == 'lizard':
            print(f"user option was: {user_option}, and computer option was: {computer_option}")
            computer_wins += 1
            print("Computer Wins!!")

    #Continue on the game loop
    continue_playing = input("do you want to continue playing? : [Y]es or [N]o: ").lower()
    if continue_playing in ('yes', 'y'):
        user_option = input(f"\nchose an option:{option_set}: ").lower()
        continue_playing == True
    elif continue_playing in ('no', 'n'):
        continue_playing == False
        print(f"FINAL SCORE: \n User Victories: {user_wins}, \n COmputer Victories: {computer_wins}")
        exit()
    else:
        print("Exiting program, you selected a wrong answer")
        print(f"FINAL SCORE: \n User Victories: {user_wins}, \n COmputer Victories: {computer_wins}")
        exit()