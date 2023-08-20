import os
import requests
import cowsay

from tabulate import tabulate
from datetime import datetime


# Make sure access key is set
if not os.environ.get("ACCESS_KEY"):
    raise RuntimeError("ACCESS_KEY not set")


def main():
    print()
    print("Welcome to PyWeather, the Python Weather App")
    print("To exit the app, press CTRL+D")

    while True:
        try:
            print()
            print("Please enter the city to find out its weather")
            city = input("Enter city: ").strip().lower()

            while True:
                try:
                    print()
                    print("Please enter your desired unit")
                    print("It can be Metric (M), Fahrenheit (F) or Scientific (S)")
                    unit = check_unit(input("Enter unit: ").strip().lower())
                    break
                except ValueError:
                    pass

            try:
                print()
                weather = lookup(city, unit)
                print(weather["query"])
                table = tabulate(make_table(weather, unit), tablefmt="heavy_outline")
                print(table)
            except:
                print("This city does not exist :(")

        except EOFError:
            print()
            print()
            cowsay.tux("Thank you for using my app. Hope you liked it :)")
            break


def lookup(city, unit):
    access_key = os.environ.get("ACCESS_KEY")
    url = f"http://api.weatherstack.com/current?access_key={access_key}&query={city}&units={unit}"
    response = requests.get(url)
    result = response.json()

    weather = {}

    query = result["request"]["query"]
    localtime = result["location"]["localtime"]
    temp = result["current"]["temperature"]
    feelslike = result["current"]["feelslike"]
    wind_speed = result["current"]["wind_speed"]
    wind_degree = result["current"]["wind_degree"]
    wind_dir = result["current"]["wind_dir"]
    pressure = result["current"]["pressure"]
    precip = result["current"]["precip"]
    humidity = result["current"]["humidity"]
    cloudcover = result["current"]["cloudcover"]
    uv_index = result["current"]["uv_index"]
    visibility = result["current"]["visibility"]

    weather.update(
        {
            "query": query,
            "localtime": localtime,
            "temp": temp,
            "feelslike": feelslike,
            "wind_speed": wind_speed,
            "wind_degree": wind_degree,
            "wind_dir": wind_dir,
            "pressure": pressure,
            "precip": precip,
            "humidity": humidity,
            "cloudcover": cloudcover,
            "uv_index": uv_index,
            "visibility": visibility,
        }
    )

    return weather


def check_unit(unit):
    if unit in ("m", "metric"):
        return "m"
    elif unit in ("f", "fahrenheit"):
        return "f"
    elif unit in ("s", "scientific"):
        return "s"
    else:
        print("Please enter a correct unit: Metric (M), Fahrenheit (F) or Scientific (S)")
        raise ValueError


def convert_time(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    date = date_obj.strftime("%B %d, %I:%M %p")
    return date


def make_table(data, unit):
    if unit == "m":
        values = [
            ["🕔 Local Time", convert_time(data["localtime"])],
            ["🌡️  Temperature", f"{data['temp']}°C"],
            ["🌤️  Feels Like", f"{data['feelslike']}°C"],
            ["🍃 Wind Speed", f"{data['wind_speed']} km/h"],
            ["🧭 Wind Degree", f"{data['wind_degree']}°"],
            ["🧭 Wind Direction", f"{data['wind_dir']}"],
            ["💨 Pressure", f"{data['pressure']} mb"],
            ["🌧️  Precipitation", f"{data['precip']} mm"],
            ["💧 Humidity", f"{data['humidity']}%"],
            ["☁️  Cloud Cover", f"{data['cloudcover']}%"],
            ["☀️  UV Index", f"{data['uv_index']}"],
            ["👀 Visibility", f"{data['visibility']} km"],
        ]
    elif unit == "f":
        values = [
            ["🕔 Local Time", convert_time(data["localtime"])],
            ["🌡️  Temperature", f"{data['temp']}°F"],
            ["🌤️  Feels Like", f"{data['feelslike']}°F"],
            ["🍃 Wind Speed", f"{data['wind_speed']} mph"],
            ["🧭 Wind Degree", f"{data['wind_degree']}°"],
            ["🧭 Wind Direction", f"{data['wind_dir']}"],
            ["💨 Pressure", f"{data['pressure']} mb"],
            ["🌧️  Precipitation", f"{data['precip']} in"],
            ["💧 Humidity", f"{data['humidity']}%"],
            ["☁️  Cloud Cover", f"{data['cloudcover']}%"],
            ["☀️  UV Index", f"{data['uv_index']}"],
            ["👀 Visibility", f"{data['visibility']} mi"],
        ]
    else:
        values = [
            ["🕔 Local Time", convert_time(data["localtime"])],
            ["🌡️  Temperature", f"{data['temp']} K"],
            ["🌤️  Feels Like", f"{data['feelslike']} K"],
            ["🍃 Wind Speed", f"{data['wind_speed']} km/h"],
            ["🧭 Wind Degree", f"{data['wind_degree']}°"],
            ["🧭 Wind Direction", f"{data['wind_dir']}"],
            ["💨 Pressure", f"{data['pressure']} mb"],
            ["🌧️  Precipitation", f"{data['precip']} mm"],
            ["💧 Humidity", f"{data['humidity']}%"],
            ["☁️  Cloud Cover", f"{data['cloudcover']}%"],
            ["☀️  UV Index", f"{data['uv_index']}"],
            ["👀 Visibility", f"{data['visibility']} km"],
        ]

    return values


if __name__ == "__main__":
    main()
