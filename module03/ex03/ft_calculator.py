class calculator:
    """
    Description:    Class with automatic operations

    Attributes:
            - values(list): List of numbers
    Methods:
            - mul : Multiply the values by the parameter
            - add : Sum the values by the parameter
            -sub

    """

    def __init__(self, values):
        self.values = values

    def __mul__(self, value):
        self.values = [values * value for values in self.values]
        print(self.values)

    def __add__(self, value):
        self.values = [values + value for values in self.values]
        print(self.values)

    def __sub__(self, value):
        self.values = [values - value for values in self.values]
        print(self.values)

    def __truediv__(self, value):
        if value is 0:
            return print("Error: Division by 0 is not authorized !")
        self.values = [values / value for values in self.values]
        print(self.values)


def main():

    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * "hugo"
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    return 0


if __name__ == "__main__":
    main()
