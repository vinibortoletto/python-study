import random
import json


def get_pokemon_name(file):
    pokemon_list = json.load(file)["results"]
    pokemon_obj = random.choice(pokemon_list)
    pokemon_name = pokemon_obj["name"].lower()

    return pokemon_name


# def print_clue(guess_counter, pokemon_name):
#     clue = ""

#     for index in range(0, guess_counter):
#         clue += pokemon_name[index]

#     print(clue)


# if __name__ == "__main__":
#     with open("pokemons.json") as file:
#         pokemon_name = get_pokemon_name(file)
#         guess_counter = 0
#         guess_limit = len(pokemon_name) - 1

#         while True:
#             user_guess = input("Who's that pokemon? ")

#             if user_guess == pokemon_name:
#                 print(f"Right! It's {pokemon_name.upper()}!")
#                 break

#             elif guess_counter == guess_limit:
#                 print(f"Sorry. The pokemon was {pokemon_name.upper()}")
#                 break

#             else:
#                 print("Wrong! Try again.")
#                 guess_counter += 1
#                 print_clue(guess_counter, pokemon_name)

if __name__ == "__main__":
    with open("pokemons.json") as file:
        pokemon_name = get_pokemon_name(file)
        guess_counter = 0
        guess_limit = len(pokemon_name) - 1

        while guess_counter < guess_limit:
            user_guess = input("Who's that pokemon? ")

            if user_guess == pokemon_name:
                print(f"Right! It's {pokemon_name.upper()}!")
                break

            else:
                print("Wrong! Try again.")
                guess_counter += 1
                print(pokemon_name[:guess_counter])

        else:
            print(f"Sorry. The pokemon was {pokemon_name.upper()}")
