import sys


def count_characters(input_string):
    """
    Count the types of characters in a given string.

    Parameters:
    input_string (str): The string to analyze.

    Returns:
    dict: A dictionary containing counts of character types.
    """

    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    counts = {
        "upper": sum(1 for char in input_string if char.isupper()),
        "lower": sum(1 for char in input_string if char.islower()),
        "punct": sum(1 for char in input_string if char in punctuation),
        "spaces": sum(
            1 for char in input_string if char.isspace()
        ),  # inclut espaces, tabulations, retours à la ligne, etc.
        "digits": sum(1 for char in input_string if char.isdigit()),
    }
    return counts


def display_character_counts(input_string):
    """
    Display the counts of different character types for a given string.

    Parameters:
    input_string (str): The string to analyze and display the counts.
    """
    counts = count_characters(input_string)
    total_chars = len(input_string)
    print(f"The text contains {total_chars} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punct']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def main():
    """
    Main function to handle user input and execute the program.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument are provided"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)

    if len(sys.argv) == 2:
        input_string = sys.argv[1]
    else:
        print("What is the text to count?")
        input_string = sys.stdin.read()

    display_character_counts(input_string)


if __name__ == "__main__":
    main()
