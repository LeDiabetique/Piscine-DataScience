class calculator:
    """
    Description:    Class with automatic operations

    Attributes:
            - values(list): List of numbers
    Methods:
            - mul : Multiply the values by the parameter
            - add : Sum the values by the parameter
            - sub : Subtract the values by the parameter
            - truediv : Divide the values by the parameter
    """
    def __init__(self, values):
        """
        Description:    Constructor of the class

        Args:
            - values(list): List of numbers
        """
        self.values = values

    def __mul__(self, value):
        """
        Description:    Multiply the values by the parameter
        and print the values.

        Args:
            - value(float | int): Value to multiply
        """
        self.values = [values * value for values in self.values]
        print(self.values)

    def __add__(self, value):
        """
        Description:    Sum the values by the parameter
        and print the values.

        Args:
            - value(float | int): Value to add
        """
        self.values = [values + value for values in self.values]
        print(self.values)

    def __sub__(self, value):
        """
        Description:    Subtract the values by the parameter
        and print the values.

        Args:
            - value(float | int): Value to subtract
        """
        self.values = [values - value for values in self.values]
        print(self.values)

    def __truediv__(self, value):
        """
        Description:    Divide the values by the parameter
        and print the values.

        Args:
            - value(float | int): Value to divide
        """
        if value == 0:
            return print("Error: Division by 0 is not authorized !")
        self.values = [values / value for values in self.values]
        print(self.values)


def main():
    return 0


if __name__ == "__main__":
    main()
