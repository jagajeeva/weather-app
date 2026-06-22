import json
import urllib.request
import urllib.error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
API_KEY = "b778e1a78f697ef2dca2939f8df5675b"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))

    if data["cod"] == 200:
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather = data["weather"][0]["description"]

        print("\n------ Weather Report ------")
        print(f"City        : {city_name}, {country}")
        print(f"Temperature : {temperature}°C")
        print(f"Humidity    : {humidity}%")
        print(f"Wind Speed  : {wind_speed} m/s")
        print(f"Condition   : {weather}")
    else:
        print("City not found!")

except Exception as e:
    print("Error:", e)