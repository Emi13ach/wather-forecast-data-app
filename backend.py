import requests
import os

API_KEY = os.getenv("API_OPENWEATHER")


def get_data(city, forcast_days=None, options=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = forcast_days * 8
    filtered_data = filtered_data[:nr_values]
    if options == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if options == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == '__main__':
    data = get_data(city="Białystok", forcast_days=2, options="Sky")
    print(data)
