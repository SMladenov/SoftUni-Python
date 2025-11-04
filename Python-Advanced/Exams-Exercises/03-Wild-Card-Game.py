#Wild Card Game

def draw_cards(*args, **kwargs):
    
    dicCards = {}

    for name, type in args:
        if type not in dicCards.keys():
            dicCards[type] = [name]
        else:
            dicCards[type].append(name)

    for name, type in kwargs.items():
        if type not in dicCards.keys():
            dicCards[type] = [name]
        else:
            dicCards[type].append(name)

    isMonster = False
    isSpell = False
    
    if 'monster' in dicCards.keys():
        listCardsMonster = list(sorted(dicCards['monster'], reverse=True))
        isMonster = True
    if 'spell' in dicCards.keys():
        listCardsSpell = list(sorted(dicCards['spell']))
        isSpell = True

    listToPrint = []

    if isMonster:
        listToPrint.append("Monster cards:")
        for card in listCardsMonster:
            listToPrint.append(f"  ***{card}")
    if isSpell:
        listToPrint.append("Spell cards:")
        for card in listCardsSpell:
            listToPrint.append(f"  $$${card}")

    return '\n'.join(listToPrint)

print(draw_cards(("cyber dragon", "monster"), freeze="spell",))

print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))

print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
