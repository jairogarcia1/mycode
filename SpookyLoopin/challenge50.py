#!/usr/bin/env python3
## create file object in "r"ead mode
#file = input("Enter the name of a file: -->")
import time
count = 0
with open("dracula.txt", "r") as f:
    ## readlines() creates a list by reading target
     with open("vampirelines.txt","w") as fang:
    
        for line in f:
            if "vampire" in line.lower():
        
                print(line)
                count += 1
                fang.write(line)
print(count)

            #time.sleep(1)
            

    
