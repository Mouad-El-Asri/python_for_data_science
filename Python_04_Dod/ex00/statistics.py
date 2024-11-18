from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate and print various statistical measures for the given arguments.

    Parameters:
    *args (Any): A variable number of numerical arguments.
    **kwargs (Any): Keyword arguments specifying which statistics to print.

    Returns:
    None

    Prints:
    The requested statistical measures based on the provided keyword arguments.
    """
    args_len = len(args)
    if args_len == 0 or not all(isinstance(arg, int | float) for arg in args):
        for key in kwargs:
            print('Error')
        return

    sorted_args = sorted(args)

    mean = sum(sorted_args) / args_len
    median = sorted_args[args_len // 2] if args_len % 2 != 0 else \
        (sorted_args[args_len // 2] + sorted_args[args_len // 2 - 1]) // 2
    q1 = float(sorted_args[args_len // 4])
    q3 = float(sorted_args[args_len // 4 * 3])
    std = (sum([(num - mean) ** 2 for num in sorted_args]) / args_len) ** .5
    var = sum([(num - mean) ** 2 for num in sorted_args]) / args_len

    statistics = {
        'mean': mean,
        'median': median,
        'quartile': [q1, q3],
        'std': std,
        'var': var
    }

    for value in kwargs.values():
        if value in statistics:
            print(f'{value} : {statistics[value]}')
