import json

weather_api_key = ""
result = None
formatted_result = ""
print("API: " + weather_api_key)
print(result)
print(formatted_result)


def get_targets():
    file = open("monitor_targets")
    for element in file:
        print(element)


get_targets()
