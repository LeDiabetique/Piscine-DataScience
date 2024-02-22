def ft_filter(function, iterable):
    """
    Description:
    Filter elements from an iterable
    Args:
    function (function): function to apply to the elements
    iterable (iterable): elements to filter
    Return:
    list: list of the elements that passed the test
    """
    result = []
    for i in iterable:
        if function(i) is True:
            result.append(i)
    return result


def main():
    return


if __name__ == "__main__":
    main()
