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
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, weather_api_key)
    url_result = requests.get(url)
    return url_result.json()


def target_api_calls(targets, weather_api_key):
    results = {}
    for location in targets:
        results[location] = get_data(location, weather_api_key)
    return results


def print_json_pretty(data):
    print("JSON DATA :\n{}".format(json.dumps(data, indent=4)))


def process_json(json_data):
    result = {}
    for element in json_data:
        print("LOCATION  : {}".format(element))
        result[element] = process_json_element(json_data[element])
    return result


def process_json_element(json_element):


def main():
    weather_api_key = get_api_key()
    targets = get_targets()
    json_data = target_api_calls(targets, weather_api_key)

    target_elements = process_json(json_data)

    for target_element in target_elements:
        print("{} : {}".format(target_element.ljust(15), target_elements[target_element]))


main()
