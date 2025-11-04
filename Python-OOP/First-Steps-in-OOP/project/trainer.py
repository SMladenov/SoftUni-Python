from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: list[Pokemon] = []

    
    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return f"This pokemon is already caught"
        
    def release_pokemon (self, pokemon_name: str):
        for currentPokemon in self.pokemons:
            if currentPokemon.name == pokemon_name:
                self.pokemons.remove(currentPokemon)
                return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        listToOutput = []
        listToOutput.append(f"Pokemon Trainer {self.name}")
        listToOutput.append(f"Pokemon count {len(self.pokemons)}")

        for currentPokemon in self.pokemons:
            listToOutput.append(f"- {currentPokemon.pokemon_details()}")
    
        return "\n".join(listToOutput)

# pokemon = Pokemon("Pikachu", 90)

# print(pokemon.pokemon_details())

# trainer = Trainer("Ash")

# print(trainer.add_pokemon(pokemon))

# second_pokemon = Pokemon("Charizard", 110)

# print(trainer.add_pokemon(second_pokemon))

# print(trainer.add_pokemon(second_pokemon))

# print(trainer.release_pokemon("Pikachu"))

# print(trainer.release_pokemon("Pikachu"))

# print(trainer.trainer_data())
