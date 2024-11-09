from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A class representing the King Joffrey Baratheon character."""
    def get_eyes(self):
        """A getter for the eyes attribute."""
        return self.eyes

    def set_eyes(self, eyes):
        """A setter for the eyes attribute."""
        self.eyes = eyes

    def get_hairs(self):
        """A getter for the hairs attribute."""
        return self.hairs

    def set_hairs(self, hairs):
        """A setter for the hairs attribute."""
        self.hairs = hairs
