def slice_me(family: list, start: int, end: int) -> list:
    """
    Découpe un tableau 2D selon les indices start et end, et affiche sa forme avant/après.

    Args:
        family (list): Tableau 2D à découper.
        start (int): Indice de début pour le découpage.
        end (int): Indice de fin pour le découpage.

    Returns:
        list: Tableau 2D tronqué.

    Raises:
        ValueError: Si family n'est pas un tableau 2D valide ou si les sous-listes n'ont pas la même taille.
    """
    # Vérifie que family est une liste de listes non vide
    if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
        raise ValueError("L'entrée doit être un tableau 2D (liste de listes).")

    # Vérifie que toutes les sous-listes ont la même taille
    if len(family) > 0:
        row_length = len(family[0])
        if not all(len(row) == row_length for row in family):
            raise ValueError("Toutes les sous-listes doivent avoir la même taille.")

    # Affiche la forme originale
    shape = (len(family), len(family[0])) if len(family) > 0 else (0, 0)
    print(f"My shape is : {shape}")

    # Effectue le découpage
    sliced_family = family[start:end]

    # Affiche la nouvelle forme
    new_shape = (len(sliced_family), len(sliced_family[0])) if len(sliced_family) > 0 else (0, 0)
    print(f"My new shape is : {new_shape}")

    return sliced_family
