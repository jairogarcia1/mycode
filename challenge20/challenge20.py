#!/usr/bin/env python3
wordbank= ["indentation", "spaces"]

tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

wordbank.append(4)

#print(wordbank)

num = int(input("Choose a number between 0 and 18: "))

student_name= tlgstudents[num]

print(tlgstudents[0] + " always uses " + num.__str__() + " spaces to indent.")
