from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Description : Class King, inherits from Baratheon and Lannister

    Attributes:
            - first_name: str
            - is_alive: bool
            - eyes: str
            - hairs: str
            - family_name: str

    Methods:
            - set_eyes: Set the eyes color
            - set_hairs: Set the hairs color
            - get_eyes: Get the eyes color
            - get_hairs: Get the hairs color
    """
    def __init__(self, first_name, is_alive=True):
        """
        Description : Constructor of King class

        Args:
                - first_name: str
                - is_alive: bool (default: True)

        Attributes:
                - family_name: str
                - eyes: str
                - hairs: str
        """
        super().__init__(first_name, is_alive)
        
    def set_eyes(self, eyes):
        """
        Description : Set the eyes color

        Args:
                - eyes: str
        """
        self.eyes = eyes

    def set_hairs(self, hairs):
        """
        Description : Set the hairs color

        Args:
                - hairs: str
        """
        self.hairs = hairs

    def get_eyes(self):
        """
        Description : Get the eyes color

        Returns:
                - str: eyes color
        """
        return self.eyes

    def get_hairs(self):
        """
        Description : Get the hairs color

        Returns:
                - str: hairs color
        """
        return self.hairs


def main():
    return 0


if __name__ == "__main__":
    main()
