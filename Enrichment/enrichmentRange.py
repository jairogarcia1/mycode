#!/usr/bin/env python3
""" Alta3 Research | Jgarcia | range excersice"""


def main():

    bottles = int(input("How many bottles are there? \n >"))

    ## trying to print this error message
    if bottles > 100:
        print("Enter a number less than 100!")
      
    else:
        for i in range(bottles, 0, -1):
            print(f"{i} bottles of beer on the wall!")
            print(f"{i} bottles of beer on the wall! {i} bottles of beer! You take one down, pass it around!")

if __name__ == "__main__":
    main()
