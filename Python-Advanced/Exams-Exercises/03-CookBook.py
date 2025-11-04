#Cookbook

def cookbook (*args):

    dicCuisine = {}
    
    for recipeName, cuisine, ingredients in args:
        if cuisine not in dicCuisine.keys():
            dicCuisine[cuisine] = {recipeName: ingredients}
        else:
            if recipeName not in dicCuisine[cuisine].keys():
                dicCuisine[cuisine][recipeName] = ingredients

    listResult = []
    
    dicCuisineSorted = dict(sorted(dicCuisine.items(), key=lambda x: (-len(x[1]), x[0])))
    
    for cuisine, recipe in dicCuisineSorted.items():
        currentSortedDic = dict(sorted(recipe.items(), key=lambda x: x[0]))
        
        result = f"{cuisine} cuisine contains {len(currentSortedDic)} recipes:\n"
        
        for recipeName, ingredients in currentSortedDic.items():
            tempResult = f"  * {recipeName} -> Ingredients: {', '.join(ingredients)}\n"
            result += tempResult

        listResult.append(result)
    
    return ''.join(listResult)

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))
