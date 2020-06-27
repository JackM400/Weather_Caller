import json
import requests
import sys


def get_api_key():
    file = open("key_location")
    for line in file:
        return line.strip()


def get_targets():
    targets = []
    file = open("monitor_targets")
    for element in file:
        targets.append(element.strip())
    return targets


def get_data(location, weather_api_key):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location, weather_api_key)
    url_result = requests.get(url)
    return url_result.json()



def main():
    weather_api_key = get_api_key()
    targets = get_targets()
    data = []
    for element in data:
        print(data[element])


main()
