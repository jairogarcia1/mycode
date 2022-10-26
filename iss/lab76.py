#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    
    pokeapi_slice = pokeapi["sprites"]["front_default"]
    print(pokeapi)
    print(f"\n\n{pokeapi_slice}")

    for x in pokeapi["moves"]:
        a = x["move"]["name"]
        print(a)
        

    b = len(pokeapi["game_indices"])
    print(f"\n\n {b}")
main()

