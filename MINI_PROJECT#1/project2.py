#!/usr/bin/env python3
""" Alta3 Research | Jgarcia | simple project using if elif and else rolling dice"""

#imports
import random

def main():
    #establishing the dice variable
    dice = ""

    while dice != "Yes" or dice != "y" or dice != "yes":
        # take input from the user y/n
        dice = (input("Want to roll a dice?(Yes or No) --> "))

        if dice == "y":
            roll=random.randint(1,6)
            print(f"you rolled a {roll}")
        elif dice == "yes":
            roll=random.randint(1,6)
            print(f"you rolled a {roll}")
        elif dice == "Yes":
            roll=random.randint(1,6)
            print(f"You rolled a {roll}")
        else:
            print("Thanks for playing!")
        break

if __name__ == "__main__":
    main()
