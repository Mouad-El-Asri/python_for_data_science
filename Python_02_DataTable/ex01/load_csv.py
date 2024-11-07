import pandas as pd
import os as os


def load(path: str) -> pd.DataFrame:
    """
        Load a CSV file into a DataFrame.

        Args:
            path (str): The file path to the CSV file.

        Returns:
            pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        if not isinstance(path, str):
            raise TypeError('the path is not a string.')
        elif not os.path.isfile(path):
            raise FileNotFoundError(f'The file \'{path}\' does not exist, '
                                    'or is not a valid file.')
        elif not path.lower().endswith('.csv'):
            raise ValueError('the file is not a CSV file.')
        elif not os.access(path, os.R_OK):
            raise PermissionError('the file doesn\'t have read permessions.')

        pd.set_option('display.max_rows', 8)
        pd.set_option('display.max_columns', 8)
        pd.set_option('display.show_dimensions', False)

        df = pd.read_csv(path)
        print(f'Loading dataset of dimensions {df.shape}\n')

        return df
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        return None
