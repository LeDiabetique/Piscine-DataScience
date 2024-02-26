def ft_statistics(*args, **kwargs) -> None:
    """
    Description:
        This function takes in a list of numeric values
        and returns the mean, median, quartile, variance
        and standard deviation of the list.

    Args:
        args: A list of integers
        kwargs: A dictionary of strings

    Raises:
        ValueError: If the args contain anything other than integers
    """
    if not all(isinstance(a, (int | float)) for a in args):
        raise ValueError("Args should only contain int or float values")
    count = len(args)
    if count == 0:
        [print("ERROR") for _ in kwargs]
        return
    list_args = sorted(args)
    mean = sum(args) / count
    variance = sum([(i - mean) ** 2 for i in args]) / count
    std = variance**0.5

    if count % 2 == 0:
        med = (
            list_args[int((count / 2) - 1)] +
            list_args[int((count / 2))]) / 2
        fquartile = (
            list_args[int((count / 4) - 1)]
            + list_args[int(count / 4)]) / 2
        tquartile = (
            list_args[int((count * 3 / 4) - 1)] + list_args[int(count * 3 / 4)]
        ) / 2
    else:
        med = list_args[int((count - 1) / 2)]
        fquartile = list_args[int((count - 1) / 4)]
        tquartile = list_args[int((count - 1) * 3 / 4)]
    quartile = [fquartile, tquartile]

    print_dict = {
        "mean": mean,
        "std": std,
        "var": variance,
        "quartile": quartile,
        "median": med,
    }
    for key, value in kwargs.items():
        if value in print_dict:
            print(f"{value} : {print_dict[value]}")


def main():
    return 0


if __name__ == "__main__":
    main()
