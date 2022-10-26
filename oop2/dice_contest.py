#!/usr/bin/python3
"""Jgarcia | Alta3 Research
   Running a simulation with our classes"""

# import our classes
from cheatdice import *

def main():
    """called at runtime"""

    # the player known as the swapper
    ## swapper = Cheat_Swapper()
    mulligan = Cheat_Mulligan()
    # the player known as the loaded_dice
    loaded_dice = Cheat_Loaded_Dice()
    
    # track scores for both players
    mulligan_score = 0
    loaded_dice_score = 0

    # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        mulligan.roll()
        loaded_dice.roll()

        mulligan.cheat()
        loaded_dice.cheat()
        """Remove # before print statements to see simulation running
           Simulation takes approximately one hour to run with print
           statements or ten seconds with print statements
           commented out"""

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if sum(mulligan.get_dice()) == sum(loaded_dice.get_dice()):
            #print("Draw!")
            pass
        elif sum(mulligan.get_dice()) > sum(loaded_dice.get_dice()):
            #print("Dice swapper wins!")
            mulligan_score+= 1
        else:
            #print("Loaded dice wins!")
            loaded_dice_score += 1
        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Mulligan won: {mulligan_score}")
    print(f"Loaded dice won: {loaded_dice_score}")

    # determine the winner
    if mulligan_score == loaded_dice_score:
        print("Game was drawn")
    elif mulligan_score > loaded_dice_score:
        print("Swapper won most games")
    else:
        print("Loaded dice won most games")

if __name__ == "__main__":
    main()

