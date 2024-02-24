from abc import ABC, abstractmethod


class Character(ABC):
    """
    Description : Abstract class Character

    Attributes:
            - first_name: str
            - is_alive: bool

    Methods:
            - die: Abstract method to set is_alive to False
    """

    def __init__(self, first_name, is_alive=True):
        print("Character __init__ called")
        """
        Description : Constructor of Character class

        Args:
                - first_name: str
                - is_alive: bool (default: True)
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Description : Abstract method die
        """
        pass


class Stark(Character):
    """
    Description : Class Stark, inherits from Character

    Attributes:
            - first_name: str
            - is_alive: bool

    Methods:
            - die: Method to set is_alive to False
    """

    def __init__(self, first_name, is_alive=True):
        """
        Description : Constructor of Stark class
        Calls the constructor of the parent class

        Args:
                - first_name: str
                - is_alive: bool (default: True)


        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Description : Method to set is_alive to False
        """
        self.is_alive = False


def main():
    return 0


if __name__ == "__main__":
    main()
