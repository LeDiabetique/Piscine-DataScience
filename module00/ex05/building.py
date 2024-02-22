import sys


def main(args):
    """
    Description:
    This function takes a string as an argument, \
counts the number of characters in it and print them.
    It also counts the number of upper and lower case \
letters, punctuation marks, spaces and digits.

    args: string to count

    return: 0
    """
    try:
        if (len(args) == 1):
            line = input("What is the text to count?\n")
            while line is None or line == "":
                line = input("What is the text to count?\n")
        elif (len(args) == 2):
            line = args[1]
        print(f"The text contains {len(line)} characters:")
        upper = sum(1 for c in line if c.isupper())
        lower = sum(1 for c in line if c.islower())
        punct_char = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        punct = sum(1 for c in line if c in punct_char)
        space = sum(1 for c in line if c.isspace())
        digit = sum(1 for c in line if c.isdigit())

        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} puntuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")
    except EOFError:
        print("\nCTRL+D intercepted")
        sys.exit(1)
    return 0


if __name__ == "__main__":
    try:
        assert len(sys.argv) <= 2, "AssertionError: more than \
one argument is provided"
    except AssertionError as e:
        print(e)
        sys.exit(1)
    main(sys.argv)
