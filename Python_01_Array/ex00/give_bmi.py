import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
     -> list[int | float]:
    """
        Calculate the Body Mass Index (BMI) for a list of heights and weights.

        Args:
            height (list[int | float]): A list of heights in meters.
            weight (list[int | float]): A list of weights in kilograms.

        Returns:
            list[int | float]: A list containing the calculated BMI values
            for each corresponding pair of height and weight.
            The BMI is calculated using the formula: weight / (height ** 2).

        Raises:
            ZeroDivisionError: If any height value is zero.
            TypeError: If the input lists contain non-numeric values or
            if the inputs are not lists.
            ValueError: If the height and weight lists have different lengths.
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError('TypeError: the input is not a list')
        elif len(height) != len(weight):
            raise ValueError('ValueError: Height and weight'
                             ' lists must be of the same length.')
        elif not all(isinstance(h, (int, float)) for h in height) or \
                not all(isinstance(w, (int, float)) for w in weight):
            raise TypeError('TypeError: input lists contain'
                            ' non-numeric values')

        height_arr = np.array(height)
        weight_arr = np.array(weight)

        if np.any(height_arr == 0):
            raise ZeroDivisionError('ZeroDivisionError: Height cannot'
                                    ' be zero.')

        return (weight_arr / height_arr ** 2).tolist()

    except (ZeroDivisionError, ValueError, TypeError) as e:
        print(e)
        exit()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Apply a BMI limit to determine if each BMI exceeds it.

        Args:
            bmi (list[int | float]): A list of BMI values.
            limit (int): The limit.

        Returns:
            list[bool]: A list of boolean values.
            Each element is `True` if the corresponding BMI
            is greater than the limit, and `False` otherwise.

        Raises:
            ValueError: If the limit is not an integer.
            TypeError: If the bmi list contains non-numeric values
            or if the inputs are not lists.
    """
    try:
        if not isinstance(bmi, list):
            raise TypeError('TypeError: bmi input is not a list')

        bmi_arr = np.array(bmi)

        if not isinstance(limit, int):
            raise TypeError('TypeError: Limit must be an integer.')
        elif not all(isinstance(el, (int, float)) for el in bmi_arr):
            raise TypeError('TypeError: input list contain non-numeric values')

        return (bmi_arr > limit).tolist()

    except TypeError as e:
        print(e)
        exit()
