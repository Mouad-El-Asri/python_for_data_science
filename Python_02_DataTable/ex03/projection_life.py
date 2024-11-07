from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def life_projections():
	life_expectancy_data = load('life_expectancy_years.csv')
	gdp_data = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')

	life_expectancy_data_1900 = life_expectancy_data['1900']
	gdp_data_1900 = gdp_data['1900']

	plt.title('1900')
	plt.xlabel('Gross Domestic Product')
	plt.ylabel('Life Expectancy')
	plt.legend()
	plt.tight_layout()
	plt.show()


def main():
	life_projections()


if __name__ == '__main__':
	main()
