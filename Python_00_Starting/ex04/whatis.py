import sys as system

try:
	if len(system.argv) > 2:
		raise AssertionError('AssertionError: more than one argument is provided')
	elif len(system.argv) == 1:
		system.exit()
	elif not system.argv[1].isdigit() and \
		not (system.argv[1].startswith('-') and system.argv[1][1:].isdigit()):
		raise AssertionError('AssertionError: argument is not an integer')

	num = int(system.argv[1])
	if num % 2 == 0:
		print('I\'m Even.')
	else:
		print('I\'m Odd.')
except AssertionError as e:
	print(e)
