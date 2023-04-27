import json

with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

grass_type_pokemons = [pokemons for pokemon in pokemons if "Grass" in pokemon["type"]]

with open("grass_pokemons.json", mode="w") as file:
    json.dump(grass_type_pokemons, file)
