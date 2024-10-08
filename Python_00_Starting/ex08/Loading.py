def ft_tqdm(lst: range) -> None:
    """
        Displays a progress bar for a given range.

        Args:
            lst (range): The range of items to process.
    """
    total = len(lst)
    bar_length = 100
    for i, item in enumerate(lst):
        percent = (i + 1) / total
        filled_content = int(bar_length * percent)
        bar = '█' * filled_content + ' ' * int(bar_length - filled_content)
        print(f'\r{percent:.0%}|{bar}| {i + 1}/{total}', end='')
        yield item
