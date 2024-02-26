def callLimit(limit: int):
    """
    Description:
    1. The callLimit function is the decorator.
    2. The callLimiter function is the actual decorator
    that takes the function to be decorated.
    3. The limit_function function is the wrapper that checks if
    the function has been called more than the limit.

    The nonlocal keyword is used to declare that the count
    variable is not local to the limit_function function but
    is in the callLimiter function.
    """
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                return print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter


def main():
    return 0


if __name__ == "__main__":
    main()
