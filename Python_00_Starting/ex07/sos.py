import sys as system


def main():
    """
        Converts a single input string to Morse code.

        Expects one command-line argument:
            An alphanumeric string.

        Raises:
            AssertionError: If arguments are invalid.
    """
    try:
        if len(system.argv) != 2 or not \
           system.argv[1].replace(' ', '').isalnum():
            raise AssertionError('AssertionError: the arguments are bad')

        str = system.argv[1].upper()
        NESTED_MORSE = {' ': '/ ', 'A': '.- ', 'B': '-... ', 'C': '-.-. ',
                        'D': '-.. ', 'E': '. ', 'F': '..-. ', 'G': '--. ',
                        'H': '.... ', 'I': '.. ', 'J': '.--- ', 'K': '-.- ',
                        'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ',
                        'P': '.--. ', 'Q': '--.- ', 'R': '.-. ', 'S': '... ',
                        'T': '- ', 'U': '..- ', 'V': '...- ', 'W': '.-- ',
                        'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. ',
                        '0': '----- ', '1': '.---- ', '2': '..--- ',
                        '3': '...-- ', '4': '....- ', '5': '..... ',
                        '6': '-.... ', '7': '--... ', '8': '---.. ',
                        '9': '----. '
                        }
        morse_code = ''
        for char in str:
            morse_code += NESTED_MORSE[char]
        print(morse_code.strip())
    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    main()
