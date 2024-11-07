from load_csv import load
import matplotlib.pyplot as plt


def aff_life(path: str) -> None:
    """
        Plots life expectancy projections for Morocco.

        Args:
            path (str): The file path to the data containing
            life expectancy information.
    """
    df = load(path)
    df_country = df.query('country == "Morocco"')
    df_country = df_country.drop('country', axis='columns').transpose()

    df_country.plot(kind='line', figsize=(8, 6))

    plt.title('Morocco Life Expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.tight_layout()
    plt.show()


def main():
    aff_life('life_expectancy_years.csv')


if __name__ == '__main__':
    main()
