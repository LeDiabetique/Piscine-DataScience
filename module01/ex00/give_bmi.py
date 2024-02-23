import sys


def give_bmi(height: list[int | float], weight: list[int | float])\
      -> list[int | float]:
    """
    Description:
            - This function takes two lists of height and weight and
            returns a list of BMI values for each person.
    Args:
            - height: list[int | float]
            - weight: list[int | float]
    Returns:
            - list[int | float]: list of BMI values for each person
    """
    if len(height) != len(weight):
        print("Error: The number of heights and weights should be the same.")
        sys.exit(1)
    if not all(isinstance(i, (int, float)) for i in height) or \
        not all(isinstance(i, (int, float)) for i in weight) or \
            not isinstance(height, list) or not isinstance(weight, list):
        print("Error: The height and weight should be a list of int or float.")
        sys.exit(1)
    if any(i <= 0 for i in height) or any(i <= 0 for i in weight):
        print("Error: The height and weight should be greater than 0.")
        sys.exit(1)
    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / (height[i] ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Description:
            - This function takes a list of BMI values and a limit and
            returns a list of boolean values indicating whether each
            person's BMI is above the limit.
    Args:
            - bmi: list[int | float]
            - limit: int
    Returns:
            - list[bool]: list of boolean values indicating whether each
                    person's BMI is above the limit
    """
    if not all(isinstance(i, (int, float)) for i in bmi) or \
            not isinstance(bmi, list):
        print("Error: The BMI should be a list of int or float.")
        sys.exit(1)
    if not isinstance(limit, int):
        print("Error: The limit should be an integer.")
        sys.exit(1)
    if limit <= 0:
        print("Error: The limit should be greater than 0.")
        sys.exit(1)
    result = []
    for people in bmi:
        if people > limit:
            result.append(True)
        else:
            result.append(False)
    return result


def main():
    return 0


if __name__ == "__main__":
    main()
