def square(x: int | float) -> int | float:
    """
    Returns the square of the given number.

    Parameters:
    x (int | float): The number to be squared.

    Returns:
    int | float: The square of the number.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Returns the number raised to the power of itself.

    Parameters:
    x (int | float): The base number.

    Returns:
    int | float: The number raised to the power of itself.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns an inner function that applies the given function to the number.

    Parameters:
    x (int | float): The number to be processed.
    function (callable): The function to apply to the number.

    Returns:
    object: The inner function.
    """
    def inner() -> float:
        """
        Applies the given function to the number and returns the result.

        Returns:
        float: The result of applying the function to the number.
        """
        nonlocal x
        x = function(x)
        return x
    return inner
