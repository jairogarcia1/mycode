#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    name_input = input("Please enter your name:")
    day_input = input("What day is it today?:")  

    ## print() can be given a series of objects separated by a comma
    print("Hello,", name_input, "! Happy ", day_input, "!")

    print(f"Hello, {name_input}! Happy {day_input}!")
main()

