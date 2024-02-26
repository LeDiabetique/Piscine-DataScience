def square(x: int | float) -> int | float:
    """
    Description:
        Function who takes a number and returns the square of the number.
    Args:
        x: int | float

    Returns:
        int | float
    """
    return x**2


def pow(x: int | float) -> int | float:
    """
    Description:
        Function who takes a number and returns the power of the number.
    Args:
        x: int | float
    Returns:
        int | float
    """
    return x**x


def outer(x: int | float, function) -> object:
    """
    Description:
        Function who takes a number and a function and returns
        the result of the function.
        Got a inner function who takes no arguments and returns
        the result of the function.
    Args:
        x: int | float
        function: object
    Returns:
        object

    Explanation:
        We use the nonlocal keyword to declare that the x variable
        is not local to the inner function but is in the outer function.
        so in each call of the outer function, the x variable is updated.
    """

    def inner() -> float:
        nonlocal x
        x = function(x)
        return x

    return inner


def main():
    return 0


if __name__ == "__main__":
    main()
