import sys as system
from ft_filter import ft_filter


def main():
    try:
        if (len(system.argv) != 3 or not isinstance(system.argv[1], str)
           or not system.argv[2].isdigit()):
            raise AssertionError('AssertionError: the arguments are bad')
        words = system.argv[1].split(' ')
        print(ft_filter(lambda word: len(word) > int(system.argv[2]), words))
    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    main()
