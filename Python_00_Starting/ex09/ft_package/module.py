def count_in_list(lst: list[any], elem: any) -> int:
    """
        Counts the occurrences of an element in a list.

        Args:
            lst (list): The list to search in.
            elem (any): The element to count.

        Returns:
            int: The number of occurrences of the element in the list.
    """
    return lst.count(elem)
