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


def zipTract122021Data():
    df = pd.read_excel('ZIP_TRACT_122021.xlsx') #  includes zip, tract, usps_zip_pref_city, usps_zip_pref_state, res_ratio, bus_ratio, oth_ratio, tot_ratio
    # zip is zip code
    # tract is census tract
    # usps_zip_pref_city is city name in all caps
    # usps_zip_pref_state is state name in all caps
    # res_ratio is the portion of all residential deliveries within the zip code that are in the tract
    # bus_ratio is the portion of all business deliveries within the zip code that are in the tract
    # oth_ratio is the portion of all both not residential and not business deliveries within the zip code that are in the tract
    # tot_ratio is the portion of all deliveries within the zip code that are in the tract
    # cities are only in georgia and are grouped by similar zip codes and cities
    # 4818 total entries
    # print(df.shape[0])
    # print(df.head())

    print(df['usps_zip_pref_city'].nunique())

    # null_count = df.isnull().sum().sum()
    # print('Number of null values:', null_count)  # prints 0
    # there are no null values but I don't trust the zeroes and 1's in the ratio
        # columns because they seem like null values for 0's and sometimes there are
        # multiple 1's in the ratio columns which is impossible

    # res_ratioNullCount = (df['res_ratio']==0 | 1).sum()
    # print(res_ratioNullCount)
    # bus_ratioNullCount = (df['bus_ratio']==0 | 1).sum()
    # print(bus_ratioNullCount)
    # oth_ratioNullCount = (df['oth_ratio']==0 | 1).sum()
    # print(oth_ratioNullCount)
    # tot_ratioNullCount = (df['tot_ratio']==0 | 1).sum()
    # print(tot_ratioNullCount)
    # number of "null values" per column
        # res_ratio: 158 so 3.28%
        # bus_ratio: 252 so 5.23%
        # oth_ratio: 345 so 7.16%
        # tot_ratio: 247 so 5.13%

    # Means and median without removing nulls
    print('Mean res_ratio:', df['res_ratio'].mean())  # 0.169
    print('Mean bus_ratio:', df['bus_ratio'].mean())  # 0.180
    print('Mean oth_ratio:', df['oth_ratio'].mean())  # 0.166
    print('Mean tot_ratio:', df['tot_ratio'].mean())  # 0.189
    print('Median res_ratio:', df['res_ratio'].median())  # 0.0750
    print('Median bus_ratio:', df['bus_ratio'].median())  # 0.0458
    print('Median oth_ratio:', df['oth_ratio'].median())  # 0.0281
    print('Median tot_ratio:', df['tot_ratio'].median())  # 0.0801

    # means and medians after removing nulls
    df = df.drop(df[df['res_ratio'] == 0 | 1].index)
    df = df.drop(df[df['bus_ratio'] == 0 | 1].index)
    df = df.drop(df[df['oth_ratio'] == 0 | 1].index)
    df = df.drop(df[df['tot_ratio'] == 0 | 1].index)
    print('removed nulls')
    print('Mean res_ratio:', df['res_ratio'].mean())  # 0.120
    print('Mean bus_ratio:', df['bus_ratio'].mean())  # 0.118
    print('Mean oth_ratio:', df['oth_ratio'].mean())  # 0.103
    print('Mean tot_ratio:', df['tot_ratio'].mean())  # 0.121
    print('Median res_ratio:', df['res_ratio'].median())  # 0.0679
    print('Median bus_ratio:', df['bus_ratio'].median())  # 0.0371
    print('Median oth_ratio:', df['oth_ratio'].median())  # 0.0211
    print('Median tot_ratio:', df['tot_ratio'].median())  # 0.0675

    # ideas about data
        # combine data for each zip code
        # combine data for each city


if __name__ == "__main__":
    # cityData()
    zipTract122021Data()
