import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character string to be used as an ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A class representing a student."""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(default=generate_id(), init=False)

    def __post_init__(self):
        """Initialize the login attribute after the object is created."""
        self.login = self.name[0] + self.surname
