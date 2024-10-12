import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
        Slices a 2D list and returns a sublist based on the
        specified start and end indices.

        Args:
            family (list): A 2D list to be sliced.
            start (int): The starting index for the slice (inclusive).
            end (int): The ending index for the slice (exclusive).

        Returns:
            list: A new 2D list containing rows from the original list
            starting at the 'start' index up to but not including
            the 'end' index.

        Raises:
            TypeError: If the start and end lists are not integers or
            family is not a list.
            ValueError: If the provided list is not a 2D list.
    """
    try:
        if not isinstance(family, list):
            raise TypeError('The family input is not a list')
        elif not all(isinstance(lst, list) for lst in family):
            raise ValueError("The provided list is not 2D.")

        arr = np.array(family)
        print(f'My shape is : {arr.shape}')

        if not all(isinstance(el, int) for el in (start, end)):
            raise TypeError('Start and End must be integers.')

        new_arr = arr[start:end]
        print(f'My new shape is : {new_arr.shape}')
        return new_arr.tolist()
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        return []
