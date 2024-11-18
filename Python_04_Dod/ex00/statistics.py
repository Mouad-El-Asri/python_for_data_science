from typing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None:
	args_len = len(args)
	sorted_args = sorted(args)

	mean = sum(sorted_args) / args_len
	median = sorted_args[args_len // 2] if args_len % 2 != 0 else \
			(sorted_args[args_len // 2] + sorted_args[args_len // 2 - 1]) // 2

	std = (sum([(num - mean) ** 2 for num in sorted_args]) / args_len) ** .5

	if 'mean' in kwargs.values():
		print(f'mean : {mean}')
	if 'median' in kwargs.values():
		print(f'median : {median}')
	if 'quartile' in kwargs.values():
		print(f'quartile : {[]}')
	if 'std' in kwargs.values():
		print(f'std : {std}')