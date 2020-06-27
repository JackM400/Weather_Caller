import json
import requests
import sys

weather_api_key = ""
targets = []
result = None
formatted_result = ""
print("API: " + weather_api_key)
print(result)
print(formatted_result)


def get_targets():
    file = open("monitor_targets")
    for element in file:
        print(element)
        targets.append(element)


def print_targets():
    for element in targets:
        print(element)


def get_data(element):
    print(element)


get_targets()
print_targets()
