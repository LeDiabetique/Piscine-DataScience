class calculator:
    """
    Description:    Class with automatic operations

    Methods:
            - dotproduct : Calculate the dot product
            - add_vec : Add two vectors
            - sous_vec : Subtract two vectors
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Description:    Static method to calculate the dot product
        and print the result.

        Args:
            - V1(list[float]): List of numbers
            - V2(list[float]): List of numbers
        """
        tmp = 0.0
        for a in V1:
            tmp += a * V2[V1.index(a)]
        print(f"Dot product is: {tmp}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Description:    Static method to add two vectors
        and print the result.

        Args:
            - V1(list[float]): List of numbers
            - V2(list[float]): List of numbers
        """
        tmp = []
        for i in V1:
            tmp.append(i + float(V2[V1.index(i)]))
        print(f"Add Vector is : {tmp}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Description:    Static method to subtract two vectors
        and print the result.

        Args:
            - V1(list[float]): List of numbers
            - V2(list[float]): List of numbers
        """
        tmp = []
        for i in V1:
            tmp.append(i - float(V2[V1.index(i)]))
        print(f"Sous Vector is: {tmp}")


def main():
    return 0


if __name__ == "__main__":
    main()
