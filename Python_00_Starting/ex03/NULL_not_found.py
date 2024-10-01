def NULL_not_found(object: any) -> int:
	object_type = type(object)
	falsy_values = {'Nothing': 'None', 'Cheese': 'nan', 'Zero': '0', 'Empty': '', 'Fake': 'False'}
	for key, value in falsy_values.items():
		if value == str(object):
			print(f'{key}: {value} {object_type}')
			return 0
	print('Type not found')
	return 1
