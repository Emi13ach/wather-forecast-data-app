import requests
import os

API_KEY = os.getenv("API_OPENWEATHER")


def get_data(city, forcast_days=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = forcast_days * 8
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == '__main__':
    data = get_data(city="Białystok", forcast_days=2)
    print(data)
