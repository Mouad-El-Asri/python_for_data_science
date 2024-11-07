from load_csv import load
import matplotlib.pyplot as plt


def aff_pop(path: str) -> None:
    """
        Plots population projections for Morocco and Egypt.

        Args:
            path (str): The file path to the data file containing
            population data.
    """
    df = load(path)
    df_morocco = df.query('country == "Morocco"')
    df_egypt = df.query('country == "Egypt"')

    df_morocco = df_morocco.drop('country', axis='columns')
    df_egypt = df_egypt.drop('country', axis='columns')

    years = [str(year) for year in range(1800, 2051, 40)]

    df_morocco = df_morocco[years]
    df_egypt = df_egypt[years]

    df_morocco = df_morocco.map(lambda x: float(x.replace('M', '')))
    df_egypt = df_egypt.map(lambda x: float(x.replace('M', '')))

    df_morocco = df_morocco.transpose()
    df_egypt = df_egypt.transpose()

    plt.figure(figsize=(8, 6))
    plt.plot(df_morocco, label='Morocco', color='red')
    plt.plot(df_egypt, label='Egypt', color='orange')

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.tight_layout()
    plt.legend()
    plt.show()


def main():
    aff_pop('population_total.csv')


if __name__ == '__main__':
    main()
