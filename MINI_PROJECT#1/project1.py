#!/usr/bin/env python3
""" AltaResearch3 | Jgarcia | simple project using if elif and else statement"""


age = int(input("How old are you? --> "))

if age < 21:
  print("You are not allowed to buy alcohol!")
elif age == 21:
  print("You can legally buy alcohol!")
else:
  print("Dont need to see your ID")

