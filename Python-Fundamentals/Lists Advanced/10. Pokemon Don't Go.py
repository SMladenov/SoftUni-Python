#Pokemon Don't Go

pokemons = [int(i) for i in input().split()]

sum = 0

while len(pokemons) > 0:
    index = int(input())
    value = 0
    if index < 0:
        value = pokemons[0]
        sum += pokemons[0]
        pokemons[0] = pokemons[len(pokemons) - 1]
    elif index >= len(pokemons):
        value = pokemons[len(pokemons) - 1]
        sum += pokemons[len(pokemons) - 1]
        pokemons[len(pokemons) - 1] = pokemons[0]
    else:
        value = pokemons[index]
        valueToRemove = pokemons.pop(index)
        sum += valueToRemove

    pokemons = [i + value if i <= value else i - value for i in pokemons]

    #for index, i in enumerate(pokemons):
    #    if i <= value:
    #        pokemons[index] += value
    #    elif i > value:
    #        pokemons[index] -= value

print (f"{sum}")