import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Description :
    This class represents the way to play with the fields of the dataclass

    fields:
        - name: str : required
        - surname: str : required
        - active: bool : default=True
        - login: str : default=name[0].upper() + surname.lower() Can't be initialized
        - id: str : default_factory=generate_id Cant't be initialized
    """

    name: str = field(init=True)
    surname: str = field(init=True)
    if name or surname is None:
        raise ValueError("Name and surname can't be empty")
    active: bool = True
    login: str = field(init=False, default="")
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname.lower()


def main():
    return 0


if __name__ == "__main__":
    main()
