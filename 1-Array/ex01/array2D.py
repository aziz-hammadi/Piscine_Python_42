def slice_me(family: list, start: int, end: int) -> list:
    # Vérification de la validité des entrées
    """fonction qui recoit une liste et 2 parametres
    retourne une version tronquée
    si necessaire en fonction du start et du end
    et affiche les shapes avant et après la découpe"""
    """try except pour les erreurs"""
    if not isinstance(family, list) or len(family) == 0:
        raise ValueError("family doit être une liste non vide")

    if not isinstance(start, int) or not isinstance(
        end, int
    ):  # retour boolean si start et end sont des entiers
        raise ValueError("start et end doivent être des entiers")

    if not all(
        len(row) == len(family[0]) for row in family
    ):  # Vérifie si toutes les lignes ont la même longueur
        raise ValueError(
            "Toutes les lignes du tableau doivent avoir la même taille")

    # Affiche la forme de la liste (nombre de lignes et de colonnes)
    print(f"My shape is : ({len(family)}, {len(family[0])})")

    # Effectue la découpe selon les indices de start et end
    sliced_array = family[start:end]

    # Affiche la nouvelle forme après la découpe
    print(f"My new shape is : {(len(sliced_array), len(family[0]))}")

    return [row[:] for row in sliced_array]
