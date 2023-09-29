import pandas as pd
import json


def cityData():
    cities_data_file = open('cities.json')
    cities_data = json.load(cities_data_file)
    df = pd.DataFrame(cities_data)
    print(df.head())  # includes city_name, population, state, and population_density

    # json file is sorted by population density, most to least

    # print('Number of rows:', len(df))  # prints 624, numCities in GA is around that number

    # null_count = df.isnull().sum().sum()
    # print('Number of null values:', null_count)  # prints 0
    # json file has no null values

    # for i in range(0, df.shape[1]):
    #     print(df.iloc[:, i].name, df.iloc[:, i].nunique())
    # there are 624 different cities (all unique)
    # 582 different population sizes
    # all one state: GA
    # 605 different population densities

    # print('Total Population:', df['population'].sum())
    # total population in file is ~4.6 million
    # total population of state is ~10.8 million

    # print('Mean Population:', df['population'].mean())
    # print('Median Population:', df['population'].median())
    # mean population of each city is ~7400
    # median population of each city is ~1500

    # print('Mean Population Density:', df['population_density'].mean())
    # print('Median Population Density:', df['population_density'].median())
    # mean population density of each city is ~820 (in square miles?)
    # median population density of each city is ~560 (in square miles?)


if __name__ == "__main__":
    cityData()
