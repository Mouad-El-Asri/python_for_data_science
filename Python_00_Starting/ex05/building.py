import sys as system


def main():
	"""
		Analyzes a user-provided string or command-line argument, and
		counts and displays the number of characters, uppercase letters,
		lowercase letters, punctuation marks, spaces, and digits.

		Raises:
			AssertionError: If more than one command-line argument is provided.
	"""
	try:
		user_str = ''
		while len(system.argv) == 1:
			user_str = input('Enter a string: ')
			if user_str:
				break
		if len(system.argv) > 2:
			raise AssertionError('AssertionError: more than one argument is provided')
		str = user_str if user_str else system.argv[1]
		punctuation_marks = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
		print(f'The text contains {len(str)} characters:')
		print(f'{sum(1 for char in str if char.isupper())} upper letters')
		print(f'{sum(1 for char in str if char.islower())} lower letters')
		print(f'{sum(1 for char in str if char in punctuation_marks)} punctuation marks')
		print(f'{str.count(" ")} spaces')
		print(f'{sum(1 for char in str if char.isdigit())} digits')
	except AssertionError as e:
		print(e)

if __name__ == '__main__':
	main()
