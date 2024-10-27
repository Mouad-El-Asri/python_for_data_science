import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
        Load a CSV file into a DataFrame.

        Args:
            path (str): The file path to the CSV file.

        Returns:
            pd.DataFrame: A DataFrame containing the loaded data.
    """
    pd.set_option('display.max_rows', 8)
    pd.set_option('display.max_columns', 8)
    pd.set_option('display.show_dimensions', False)

    df = pd.read_csv(path)
    print(f'Loading dataset of dimensions {df.shape}')

    return df
