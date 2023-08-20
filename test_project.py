import pytest

from project import check_unit, convert_time, make_table


def test_check_unit():
    assert check_unit("m") == "m"
    assert check_unit("f") == "f"
    assert check_unit("s") == "s"
    assert check_unit("metric") == "m"
    assert check_unit("fahrenheit") == "f"
    assert check_unit("scientific") == "s"
    with pytest.raises(ValueError):
        check_unit("Python")


def test_convert_time():
    assert convert_time("2023-01-01 09:00") == "January 01, 09:00 AM"
    assert convert_time("2023-02-10 15:00") == "February 10, 03:00 PM"


def test_make_table():
    data = {
        "query": "New York, United States of America",
        "localtime": "2023-08-19 17:16",
        "temp": 26,
        "feelslike": 26,
        "wind_speed": 4,
        "wind_degree": 285,
        "wind_dir": "WNW",
        "pressure": 1016,
        "precip": 0,
        "humidity": 40,
        "cloudcover": 0,
        "uv_index": 7,
        "visibility": 16,
    }

    assert make_table(data, "m") == [
        ["🕔 Local Time", "August 19, 05:16 PM"],
        ["🌡️  Temperature", "26°C"],
        ["🌤️  Feels Like", "26°C"],
        ["🍃 Wind Speed", "4 km/h"],
        ["🧭 Wind Degree", "285°"],
        ["🧭 Wind Direction", "WNW"],
        ["💨 Pressure", "1016 mb"],
        ["🌧️  Precipitation", "0 mm"],
        ["💧 Humidity", "40%"],
        ["☁️  Cloud Cover", "0%"],
        ["☀️  UV Index", "7"],
        ["👀 Visibility", "16 km"],
    ]
