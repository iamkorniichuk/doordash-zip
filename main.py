import json

from devices import AndroidDevice
from flow import run_main_flow


if __name__ == "__main__":
    with AndroidDevice() as device:
        with open("cities.json") as file:
            cities = json.load(file)
        run_main_flow(device, cities, "results.csv")
