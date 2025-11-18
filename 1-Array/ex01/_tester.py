from array2D import slice_me

def main():
    """Fonction principale pour tester slice_me."""
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    # Tests
    print(slice_me(family, 0, 2), "\n")
    print(slice_me(family, 1, -2), "\n")
    print(slice_me(family, 1, 2), "\n")    
    print(slice_me(family, 3, 1), "\n")

if __name__ == "__main__":
    main()

#a[start:end:step]