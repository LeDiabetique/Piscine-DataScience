import sys


def check_char(arg):
    """
    Description:
    Check if the string contains only alphanumeric characters and spaces
    Args:
    arg (str): string to check
    Return:
    bool: True if the string contains only \
alphanumeric characters and spaces, False otherwise
    """
    if len(arg) == 0:
        return False
    for char in arg:
        if char.isalnum() is False and char.isspace() is False:
            return False
    return True


def ft_morse(arg):
    """
    Description:
    Print the morse code of a string
    Args:
    arg (str): string to convert to morse code
    Return:
    None
    """
    NESTED_MORSE = {
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
        " ": "/ ",
    }
    str_morse = ""
    for char in arg:
        str_morse += NESTED_MORSE[char.upper()]
    print(str_morse.rstrip())


def main(arg):
    """
    Description:
    Main function that calls the ft_morse function
    Args:
    arg (list): string to convert to morse code
    Return: 0
    """
    ft_morse(arg[1])
    return 0


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        assert check_char(sys.argv[1]), "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    main(sys.argv)
