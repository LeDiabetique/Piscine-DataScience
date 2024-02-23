import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Description:
            - This function takes a 2D list and two integers and returns a
            slice of the 2D list.
    Args:
            - family: list
            - start: int
            - end: int
    Returns:
            - list: slice of the 2D list
    """
    if not isinstance(family, list):
        print("Error: The array should be a list.")
        return None
    if not all(isinstance(i, list) for i in family):
        print("Error: The array should contain the same shape for each list.")
        return None
    if not all(len(person) > 0 for person in family):
        print("Error: The array should not contain empty lists.")
        return None
    if np.shape(family) == (0,):
        print("Error: The array should not be empty.")
        return None
    length = len(family[0])
    if not all(len(person) == length for person in family):
        print("Error: The array should be a 2D list.")
        return None
    if not isinstance(start, int) or not isinstance(end, int):
        print("Error: The start and end should be integers.")
        return None
    print(f"My shape is : {np.shape(family)}")
    print(f"My new shape is : {np.shape(family[start:end])}")
    return (family[start:end])


def main():
    return 0


if __name__ == "__main__":
    main()
