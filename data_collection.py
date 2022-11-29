import get_housing_data
import json
import random
import os
import sys


def get_data(rapid_api_key):
    cities_data_file = open('cities.json')
    cities_data = json.load(cities_data_file)
    random.shuffle(cities_data)
    for city in cities_data:
        if os.path.exists(f'data/{city["city"]}_{city["state"]}.csv'):
            continue
        get_housing_data_city(
            city['city'], city['state'], rapid_api_key)


def get_housing_data_city(city, state_code, rapid_api_key):
    results = get_housing_data.fetch_data("https://us-real-estate.p.rapidapi.com/sold-homes", {"state_code": f"{state_code}", "city": f"{city}", "offset": "0", "sort": "sold_date", },
                                          {
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": "us-real-estate.p.rapidapi.com"
    })
    df = get_housing_data.results_to_df(results)
    df.to_csv(f'data/{city}_{state_code}.csv')


if __name__ == "__main__":
    get_data(rapid_api_key=sys.argv[1])
