from give_bmi import give_bmi, apply_limit


def run_tests():
    print("=== Tests valides ===")
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print("BMI calculés :", bmi, type(bmi))
        print("apply_limit :", apply_limit(bmi, 26))
    except Exception as e:
        print(f"Erreur inattendue (cas valide) : {e}")

    try:
        height = [1.80, 1.65, 1.60]
        weight = [70, 60, 50]
        bmi = give_bmi(height, weight)
        print("BMI calculés :", bmi)
        print("apply_limit (limite=25) :", apply_limit(bmi, 25))
    except Exception as e:
        print(f"Erreur inattendue (cas valide 2) : {e}")

    print("\n=== Tests limites ===")
    try:
        height = []
        weight = []
        bmi = give_bmi(height, weight)
        print("Listes vides :", bmi)
    except Exception as e:
        print(f"Erreur attendue (listes vides) : {e}")

    try:
        height = [1e-5]
        weight = [70]
        bmi = give_bmi(height, weight)
        print("Valeurs extrêmes :", bmi)
    except Exception as e:
        print(f"Erreur inattendue (valeurs extrêmes) : {e}")

    print("\n=== Tests erreurs ===")
    try:
        height = [1.80]
        weight = [70, 80]  # longueurs différentes
        print(give_bmi(height, weight))
    except Exception as e:
        print(f"Erreur attendue (longueurs différentes) : {e}")

    try:
        height = ["1.80", 1.75]  # string au lieu de float
        weight = [70, 80]
        print(give_bmi(height, weight))
    except Exception as e:
        print(f"Erreur attendue (mauvais type dans height) : {e}")

    try:
        height = [1.80, 1.75]
        weight = [70, "80"]  # string au lieu de float
        print(give_bmi(height, weight))
    except Exception as e:
        print(f"Erreur attendue (mauvais type dans weight) : {e}")

    try:
        bmi = [22.5, 27.3]
        print(apply_limit(bmi, "25"))  # limit est string
    except Exception as e:
        print(f"Erreur attendue (limit non int) : {e}")

    try:
        bmi = [22.5, "27.3"]  # mauvais type dans bmi
        print(apply_limit(bmi, 25))
    except Exception as e:
        print(f"Erreur attendue (mauvais type dans bmi) : {e}")


if __name__ == "__main__":
    run_tests()
