#!/usr/bin/env python3
## Script to search and stop on first match
import os

## Define a function that stops searching on first match
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result
def main():
    lookfor = input("What am I looking for? ")
    lookwhere = input("What is the path in which I should search? ")

    print(find_all(lookfor, lookwhere))
main()

