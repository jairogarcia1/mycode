#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]



NE = farms[0]["agriculture"]
#for i in NE:
#    print(i)
W = farms[1]["agriculture"]
SE = farms[2]["agriculture"][0]



choice = int(input("\nChoose a number from the menu:\n 1. NE Farm\n 2. W Farm\n 3. SE Farm \n\n"))


if choice == 1:
    print(f"We raise {NE} at this farm.")
elif choice == 2:
    print(f"We raise {W} at this farm.")
elif choice == 3:
    print(f"We raise and grow {SE} at this farm.")
else:
    print("Please choose a number from the menu: \n")

