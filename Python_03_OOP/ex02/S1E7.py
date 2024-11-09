from S1E9 import Character


class Baratheon(Character):
    """A class Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """
            The constructor for the Baratheon class.

            Parameters:
                first_name (str): The first name of the character.
                is_alive (bool): A flag indicating whether the
                character is alive or not.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self) -> None:
        """A method that sets the is_alive flag to False."""
        self.is_alive = False
        print(self.first_name + " died")

    @property
    def __str__(self) -> str:
        return f"{self.first_name} {self.family_name} has {self.eyes} " \
               f"eyes and {self.hairs} hairs, " \
               f"and he/she is {'alive' if self.is_alive else 'dead'}"

    @property
    def __repr__(self) -> str:
        return f"Baratheon(first_name='{self.first_name}', " \
               f"is_alive={self.is_alive})"


class Lannister(Character):
    """A class Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """
            The constructor for the Lannister class.

            Parameters:
                first_name (str): The first name of the character.
                is_alive (bool): A flag indicating whether the
                character is alive or not.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self) -> None:
        """A method that sets the is_alive flag to False."""
        self.is_alive = False
        print(self.first_name + " died")

    @staticmethod
    def create_lannister(first_name, is_alive=True):
        """A static method that creates a Lannister character."""
        return Lannister(first_name, is_alive)

    @property
    def __str__(self) -> str:
        return f"{self.first_name} {self.family_name} has {self.eyes} " \
               f"eyes and {self.hairs} hairs, and he/she is " \
               f"{'alive' if self.is_alive else 'dead'}"

    @property
    def __repr__(self) -> str:
        return f"Lannister(first_name='{self.first_name}', " \
               f"is_alive={self.is_alive})"
