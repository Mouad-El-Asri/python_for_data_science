from typing import Any


def callLimit(limit: int):
    """
    A decorator to limit the number of times a function can be called.

    Args:
        limit (int): The maximum number of times the function can be called.

    Returns:
        function: The decorated function with call limit applied.
    """
    count = 0

    def callLimiter(function):
        """
        The actual decorator function that wraps the original function.

        Args:
            function (function): The function to be decorated.

        Returns:
            function: The wrapped function with call limit logic.
        """
        def limit_function(*args: Any, **kwds: Any):
            """
            The wrapper function that enforces the call limit.

            Args:
                *args (Any): Positional arguments for the original function.
                **kwds (Any): Keyword arguments for the original function.

            Returns:
                Any: The result of the original function call if within limit.

            Raises:
                Exception: If the function is called more than the limit.
            """
            try:
                nonlocal count
                if count >= limit:
                    raise Exception(f'Error: {function} call too many times')
                count += 1
                return function(*args, **kwds)
            except Exception as e:
                print(f'{e.__class__.__name__}: {e}')
        return limit_function
    return callLimiter
