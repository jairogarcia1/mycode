#!/usr/bin/env python3
## create file object in "r"ead mode
file = input("Enter the name of a file: -->")

with open(file, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    #configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
# print(configlist)

    x = len(configfile.readlines())
    print(x)

