NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def encode_to_morse(input_string):
    """
    Encode a string into Morse code.

    Parameters:
    input_string (str): The string to be encoded.

    Returns:
    str: The encoded Morse code representation.
    """
    assert isinstance(input_string, str), "Argument is not a string"

    try:
        encoded_message = " ".join(
            NESTED_MORSE[char.upper()]
            for char in input_string
            if char.upper() in NESTED_MORSE
        )

        assert len(encoded_message) > 0, "Invalid character(s) in input string"

        return encoded_message
    except KeyError:
        raise AssertionError("Invalid character(s) in input string")


def main():
    """
    Main function to handle the program execution.
    """
    import sys

    try:
        assert len(sys.argv) == 2, "Incorrect number of arguments"
        encoded_message = encode_to_morse(sys.argv[1])
        print(encoded_message)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
