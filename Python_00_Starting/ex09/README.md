# ft_package

A sample test package

## Building the Package

To build the **ft_package** package locally, follow these steps:

1. Make sure you have the required tools installed:
   ```bash
   pip install build
   ```
2. Run the following command to build the package:
	```
	python -m build
	```
And now it’s done! The .whl file and .tar.gz can then be distributed and installed.

```bash
dist/
    my_package-0.0.1-py3-none-any.whl
    my_package-0.0.1.tar
```

## Installation

To install **ft_package**, run the following command:
```bash
pip install dist/ft_package-1.0.0.tar.gz
```
or

```bash
pip install dist/ft_package-1.0.0-py3-none-any.whl
```

## Example Usage

The following is an example usage of **ft_package**:

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

## Author

**Mouad El Asri**  
[GitHub Profile](https://github.com/Mouad-El-Asri)  
[LinkedIn Profile](https://www.linkedin.com/in/mouad-el-asri)


## Contact

If you want to contact me you can reach me at <elasri.mouad.2002@gmail.com>.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
