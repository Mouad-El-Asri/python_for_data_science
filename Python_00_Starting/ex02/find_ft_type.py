def all_thing_is_obj(object: any) -> int:
	type_name = type(object).__name__.capitalize()
	if type_name in {'List', 'Tuple', 'Set', 'Dict'}:
		print(f'{type_name} : {type(object)}')
	elif type_name == 'Str':
		print(f'{object} is in the kitchen : {type(object)}')
	else:
		print("Type not found")
	return 42
