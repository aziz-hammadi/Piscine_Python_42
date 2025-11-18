"""
Fournit des fonctions pour calculer les valeurs d'IMC et les comparer à une limite.
"""


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calcule les valeurs d'IMC à partir de listes de tailles et de poids.

    Arguments :
        height (List[int | float]) : Liste des tailles en mètres.
        weight (List[int | float]) : Liste des poids en kilogrammes.

    Retourne :
        List[int | float] : Liste des valeurs d'IMC.

    Exceptions :
        ValueError : Si les listes n'ont pas la même taille.
        TypeError : Si les listes contiennent des éléments qui ne sont pas des int ou float.
    """
    if len(height) != len(weight):
        raise ValueError("Les listes de tailles et de poids doivent avoir la même longueur.")

    if any(h < 0 for h in height) or any(w < 0 for w in weight):
        raise ValueError("Les valeurs de taille et de poids doivent être positives.")

    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("La liste des tailles doit contenir uniquement des entiers ou des flottants.")

    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("La liste des poids doit contenir uniquement des entiers ou des flottants.")

    return [w / (h**2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Vérifie si les valeurs d'IMC dépassent une limite donnée.

    Arguments :
        bmi (List[int | float]) : Liste des valeurs d'IMC.
        limit (int) : La valeur seuil d'IMC.

    Retourne :
        List[bool] : True si l'IMC est supérieur à la limite, False sinon.

    Exceptions :
        TypeError : Si bmi contient des types invalides ou si limit n'est pas un int.
    """
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("La liste des IMC doit contenir uniquement des entiers ou des flottants.")

    if not isinstance(limit, int):
        raise TypeError("La limite doit être un entier.")

    return [b > limit for b in bmi]
