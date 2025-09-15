from piscine.python_1.ex01._array2D import slice_me

def main():
    """Fonction principale pour tester slice_me."""
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    # Tests
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

if __name__ == "__main__":
    main()
