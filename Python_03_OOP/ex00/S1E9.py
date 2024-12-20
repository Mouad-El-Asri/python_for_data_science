from abc import ABC, abstractmethod


class Character(ABC):
    """A base class representing a character."""
    def __init__(self, first_name, is_alive=True):
        """
            The constructor for the Character class.

            Parameters:
                first_name (str): The first name of the character.
                is_alive (bool): A flag indicating whether the
                character is alive or not.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die() -> None:
        """
            Abstract method to be implemented by subclasses.
            This method sets the is_alive flag to False.
        """
        pass


class Stark(Character):
    """A class representing a Stark character."""
    def die(self) -> None:
        """A method that sets the is_alive flag to False."""
        self.is_alive = False
        print(self.first_name + " died")
