#!/usr/bin/env python3

''' Alta3 Research | JGarcia Lists Challenge '''

#random module
import random

def main():
    wordbank= ["indentation", "spaces"]

    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    wordbank.append(4)

    #print(wordbank)

    #num = int(input("Choose a number between 0 and 18: "))
    num = random.randrange(0,18)
    student_name= tlgstudents[num]

    print(student_name + " always uses " + num.__str__() + " spaces to indent.")


main()
