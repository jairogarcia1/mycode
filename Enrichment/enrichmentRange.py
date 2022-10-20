#!/usr/bin/env python3
""" Alta3 Research | Jgarcia | range excersice"""


def main():

    bottles = int(input("How many bottles are there? \n >"))
    while bottles <= 100:
        for i in range(bottles, 0, -1):
            print(f"{i} bottles of beer on the wall!")
            print(f"{i} bottles of beer on the wall! {i} bottles of beer! You take one down, pass it around!")
        ## trying to print this error message
        if bottles > 100:
            print("Enter a number less than 100!")
            continue
        else:
            break
if __name__ == "__main__":
    main()
