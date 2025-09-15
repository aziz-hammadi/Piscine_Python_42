import sys

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"

    arg = sys.argv[1]
    assert arg.lstrip('-').isdigit(), "argument is not an integer"

    number = int(arg)
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except IndexError:
    pass

except AssertionError as error:
    print(f"AssertionError: {error}")
