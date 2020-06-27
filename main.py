import json
import requests
import sys
import os
from datetime import datetime


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
        result[element] = process_json_element(json_data[element])
    return result


def process_json_element(json_element):
    weather_data = json_element["weather"]
    main_data = json_element["main"]
    wind_data = json_element["wind"]

    overall = weather_data[0]["description"]
    temp = int(main_data["temp"])
    humidity = int(main_data["humidity"])
    wind_speed = int(wind_data["speed"])

    return "{},{},{},{}".format(overall, temp, humidity, wind_speed)


def get_header():
    return "Date,Location,Overall,Temperature,Humidity,Wind_Speed\n"


def csv_check():
    check = os.path.isfile("./weather_data.csv")
    if check:
        return "weather_data.csv"
    else:
        file = open("weather_data.csv", "a+")
        file.write(get_header())
        file.close()
        return "weather_data.csv"


def populate_csv(target, write_data):
    file = open(target, "a+")
    current = datetime.today().strftime('%d-%m-%Y')
    for element in write_data:
        line_element = "{},{},{}\n".format(current, element, write_data[element])
        file.write(line_element)
    file.close()


def main():
    weather_api_key = get_api_key()
    targets = get_targets()
    json_data = target_api_calls(targets, weather_api_key)

    target_elements = process_json(json_data)

    for target_element in target_elements:
        print("{} : {}".format(target_element.ljust(15), target_elements[target_element]))
    csv_file = csv_check()
    populate_csv(csv_file, target_elements)


main()
