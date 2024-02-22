import sys
from filter import ft_filter


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


def main(args):
    """
    Description:
    Main function to test the ft_filter function
    Args:
    args (list):
        args[1] (str): string to filter
        args[2] (str): minimum length of the words to keep
    Return:
    int: 0 if the function works
    """
    words = args[1].split()
    result = ft_filter(lambda x: len(x) > int(args[2]), words)
    print(result)
    return 0


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert check_char(sys.argv[1]), "the arguments are bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    main(sys.argv)
