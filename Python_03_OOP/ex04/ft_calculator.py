class calculator:
    """A class to perform basic calculations on a vector."""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""
        dot_product = sum([x * y for x, y in zip(V1, V2)])
        print(f'Dot product is: {dot_product}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors."""
        add_vec: list[float] = [float(x + y) for x, y in zip(V1, V2)]
        print(f'Add Vector is: {add_vec}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors."""
        sous_vec: list[float] = [float(x - y) for x, y in zip(V1, V2)]
        print(f'Sous Vector is: {sous_vec}')
