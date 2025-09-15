# filterstring.py
import sys
from ft_filter import ft_filter


def main():
    """
    The main function that accepts two arguments: a string S and an integer N.
    It outputs a list of words from S that have a length greater than N,
    ignoring punctuation.

    If the number of arguments is not two or if any argument has the wrong type
    it raises an AssertionError.
    """
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    try:
        # Vérification du nombre d'arguments
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"

        # Unpack et validation des arguments
        S, N = sys.argv[1], sys.argv[2]
        assert N.isdigit(), "AssertionError: the arguments are bad"
        N = int(N)

        # Suppression de la ponctuation
        cleaned_string = S.translate(str.maketrans("", "", punctuation))

        # Découpage et filtrage des mots
        words = cleaned_string.split()
        filtered_words = ft_filter(lambda word: len(word) > N, words)

        # Affichage des résultats
        print(list(filtered_words))

    except AssertionError as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
