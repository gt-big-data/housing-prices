import pandas as pd
import requests
import sys
import re
import traceback


def fetch_data(url: str, querystring: dict, headers: dict) -> list:
    """ Fetches data from an API source while ensuring requests do not exceed the free limit

    Parameters
    ----------
    url: str
        The URL of the API
    querystring: dict
        A dictionary containing query parameters for the API
    headers: dict
        A dictionary containing request headers for the API

    Returns
    -------
    list
        A list containing JSON data fetched from the API

    """

    try:

        with open('request_count.txt', 'r') as f:

            request_count = int(f.readline())

    except FileNotFoundError:

        request_count = 0

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    request_count += 1

    response.raise_for_status()

    response_json = response.json()

    result_size = int(response_json['data']['count'])

    total = int(response_json['data']['total'])

    remaining = total - result_size

    data = []

    data.extend(response_json['data']['results'])

    while remaining > 0:

        if request_count >= 300:

            print("Exceeded 300 requests! Returning retrieved data")

            break

        querystring['offset'] = str(int(querystring['offset']) + result_size)

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        request_count += 1

        try:

            response.raise_for_status()

        except requests.exceptions.HTTPError:

            print("HTTPError! Returning retrieved data")

            break

        response_json = response.json()

        result_size = int(response_json['data']['count'])

        remaining -= result_size

        print(
            f"GET {result_size} results OF TOTAL {total} WITH {remaining} remaining")

        data.extend(response_json['data']['results'])

    with open('request_count.txt', 'w') as f:

        f.write(str(request_count))

    return data


def row_to_dict(row: dict) -> dict:
    """ Converts each JSON row to a dictionary object

    Parameters
    ----------
    row: dict
        A JSON object containing each row of data fetched from the API

    Returns
    -------
    dict
        A dictionary containing relevant features from the data

    """

    row_dict = {}

    def list_date():

        row_dict['list_date'] = row['list_date']

    def list_price():

        row_dict['list_price'] = row['list_price']

    def status():

        row_dict['status'] = row['status']

    def property_id():

        row_dict['property_id'] = row['property_id']

    for key in row['flags'].keys():

        try:

            row_dict[key] = row['flags'][key]

        except TypeError:

            row_dict[key] = None

    def postal_code():

        row_dict['postal_code'] = row['location']['address']['postal_code']

    def state():

        row_dict['state'] = row['location']['address']['state']

    def state_code():

        row_dict['state_code'] = row['location']['address']['state_code']

    def city():

        row_dict['city'] = row['location']['address']['city']

    def county():

        row_dict['county'] = row['location']['county']['name']

    def address_line():

        row_dict['address_line'] = row['location']['address']['line']

    def latitude():

        row_dict['latitude'] = row['location']['address']['coordinate']['lat']

    def longitude():

        row_dict['longitude'] = row['location']['address']['coordinate']['lon']

    for key in row['description'].keys():

        try:

            row_dict[key] = row['description'][key]

        except TypeError:

            row_dict[key] = None

    def tags():

        row_dict['tags'] = row['tags']

    funcs = [list_date, list_price, status, property_id, postal_code, state,
             state_code, city, county, address_line, latitude, longitude, tags]

    for function in funcs:

        try:

            function()

        except TypeError as e:

            tb = traceback.format_exc()

            m = re.search("row_dict\[(.*?)\]", tb)

            key = m.groups()[0].split("'")[1]

            row_dict[key] = None

            print(f"Setting {key} to None")

    return row_dict


def results_to_df(results: list) -> pd.DataFrame:
    """ Creates a DataFrame from data fetched from the API

    Parameters
    ----------
    results: list
        Data fetched from the API

    Returns
    -------
    pd.DataFrame
        A DataFrame representation of the data with relevant features as columns

    """

    df = pd.DataFrame(columns=row_to_dict(results[0]).keys())

    for row in results:

        df = df.append(row_to_dict(row), ignore_index=True)

    return df.set_index('property_id')


if __name__ == '__main__':

    if len(sys.argv) < 3:

        print(f"Usage: {sys.argv[0]} <city> <state_code> <rapid_api_key>")

        exit()

    city = sys.argv[1]

    state_code = sys.argv[2]

    rapid_api_key = sys.argv[3]

    results = fetch_data("https://us-real-estate.p.rapidapi.com/sold-homes", {"state_code": f"{state_code}", "city": f"{city}", "offset": "0", "sort": "sold_date", },
                         {
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": "us-real-estate.p.rapidapi.com"
    })

    df = results_to_df(results)

    df.to_csv(f'{city}_{state_code}.csv')
