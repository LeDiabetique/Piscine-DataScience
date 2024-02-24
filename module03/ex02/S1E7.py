from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family member."""

    def __init__(
        self,
        first_name,
        is_alive=True,
        hairs="dark",
        family_name="Baratheon",
        eyes="brown",
    ):
        """
        Initialize the Baratheon family member
        """
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """
        Kill the Baratheon member
        """
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family member."""

    def __init__(
        self,
        first_name,
        is_alive=True,
        hairs="light",
        family_name="Lannister",
        eyes="blue",
    ):
        """
        Initialize the Lannister family member
        """
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def create_lannister(first_name, is_alive=False):
        """
        Description : Create a Lannister object

        Args:
                - first_name: str
                - is_alive: bool

        Returns:
                - Lannister: Lannister object
        """
        tmp = Lannister.__new__(Lannister)
        tmp.first_name = first_name
        tmp.is_alive = is_alive
        tmp.family_name = "Lannister"
        tmp.eyes = "blue"
        tmp.hairs = "light"
        return tmp

    def die(self):
        """
        Kill the Lannister family member
        """
        self.is_alive = False
