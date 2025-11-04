#Numbers Filter

def even_odd_filter(**kwargs):
    dictFiltered = {}
    for key, value in kwargs.items():
        if key == "odd":
            dictFiltered[key] = [int(i) for i in value if i % 2 == 1]
        elif key == "even":
            dictFiltered[key] = [int(i) for i in value if i % 2 == 0]

    return dict(sorted(dictFiltered.items(), key=lambda x: -len(x[1])))