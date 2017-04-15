goat = {
    'species': 'goat',
    'wild_ancestor': 'Bezoar ibex',
    'purpose': 'milk, meat, fibre, skin, show, racing, fighting, clearing land, pets'
}

sheep = {
    'species': 'sheep',
    'wild_ancestor': 'Mouflon',
    'purpose': 'fibre, meat, milk, leather, pelt, vellum, pets, show, racing, research, guarding, fighting, ornamental'
}

cattle = {
    'species': 'cattle',
    'wild_ancestor': 'Aurochs',
    'purpose': 'meat, milk, leather, hides, working, plowing, draft, vellum, blood, transportation, soil fertilization, fighting, show, pets'
}

pets = [goat, sheep, cattle]

for pet in pets:
    print(pet['species'], "\n", pet['wild_ancestor'], "\n", pet['purpose'],"\n", "\n" )