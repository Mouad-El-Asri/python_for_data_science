class calculator:
    """A class to perform basic operations on a vector."""
    def __init__(self, vector):
        """The constructor for calculator class."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a scalar to a vector."""
        self.vector = [elem + object for elem in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply a vector by a scalar."""
        self.vector = [elem * object for elem in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a scalar from a vector."""
        self.vector = [elem - object for elem in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide a vector by a scalar."""
        try:
            self.vector = [elem / object for elem in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print(f"{e.__class__.__name__}: Can't divide by zero")
