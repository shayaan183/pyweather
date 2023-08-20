# **PyWeather (Python Weather App)** - CS50P Final Project
### [**Video Demo**](https://www.youtube.com/watch?v=NtBiF9wOoJw)
### **Description:** A command-line weather app to find out about the current weather for any city you search

# **Libraries**
- [os](https://docs.python.org/3/library/os.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [requests](https://pypi.org/project/requests/)
- [tabulate](https://pypi.org/project/tabulate/)
- [cowsay](https://pypi.org/project/cowsay/)

# **Installation**
- Install all the required libraries from [requirements.txt](./requirements.txt)
- Create a free account on [weatherstack](https://weatherstack.com/) to receive your access key
- Copy and paste your access key in the terminal (swap abcde12345 with your access key)
```
$ export ACCESS_KEY=abcde12345
```
- Run the app by typing:
```
$ python project.py
```

# **Features**
- First, type in the what city's weather you want to know by typing in its name
```
Welcome to PyWeather, the Python Weather App
To exit the app, press CTRL+D

Please enter the city to find out its weather
Enter city: Toronto
```
- Then type in what units you want, Metric (M), Fahrenheit (F) or Scientific (S)
```
Please enter your desired unit
It can be Metric (M), Fahrenheit (F) or Scientific (S)
Enter unit: M
```
- You'll get a table with all the current weather information for the city you entered

```
Toronto, Canada
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃ 🕔 Local Time     ┃ August 19, 09:02 PM ┃
┃ 🌡️ Temperature    ┃ 19°C                ┃
┃ 🌤️ Feels Like     ┃ 19°C                ┃
┃ 🍃 Wind Speed     ┃ 17 km/h             ┃
┃ 🧭 Wind Degree    ┃ 220°                ┃
┃ 🧭 Wind Direction ┃ SW                  ┃
┃ 💨 Pressure       ┃ 1016 mb             ┃
┃ 🌧️ Precipitation  ┃ 0 mm                ┃
┃ 💧 Humidity       ┃ 68%                 ┃
┃ ☁️ Cloud Cover    ┃ 0%                  ┃
┃ ☀️ UV Index       ┃ 7                   ┃
┃ 👀 Visibility     ┃ 14 km               ┃
┗━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━┛
```
- You can continue to enter more city names to get their weather information or you can quit the app by pressing Ctrl+D
```
  ________________________________________________
| Thank you for using my app. Hope you liked it :) |
  ================================================
                                                     \
                                                      \
                                                       \
                                                        .--.
                                                       |o_o |
                                                       |:_/ |
                                                      //   \ \
                                                     (|     | )
                                                    /'\_   _/`\
                                                    \___)=(___/
```
