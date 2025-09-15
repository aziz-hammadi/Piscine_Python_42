def slice_me(family: list, start: int, end: int) -> list:
    # Vérification de la validité des entrées
    if not all(len(row) == len(family[0]) for row in family):  # Vérifie si toutes les lignes ont la même longueur
        raise ValueError("Toutes les lignes du tableau doivent avoir la même taille")
    
    # Affiche la forme de la liste (nombre de lignes et de colonnes)
    print(f"My shape is : {len(family)} x {len(family[0])}")
    
    # Effectue la découpe selon les indices de start et end
    sliced_array = [row[start:end] for row in family]
    
    # Affiche la nouvelle forme après la découpe
    print(f"My new shape is : {len(sliced_array)} x {len(sliced_array[0])}")
    
    return sliced_array
