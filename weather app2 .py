import tkinter as tk
import json
import urllib.request
import urllib.error
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

API_KEY = "YOUR_API_KEY"

def get_weather():
    city = city_entry.get().strip()

    if not city:
        result.config(text="Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))

        if data["cod"] == 200:
            city_name = data["name"]
            country = data["sys"]["country"]

            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]

            wind_speed = data["wind"]["speed"]

            weather = data["weather"][0]["description"].title()

            report = (
                f"City        : {city_name}, {country}\n"
                f"Temperature : {temperature}°C\n"
                f"Feels Like  : {feels_like}°C\n"
                f"Humidity    : {humidity}%\n"
                f"Pressure    : {pressure} hPa\n"
                f"Wind Speed  : {wind_speed} m/s\n"
                f"Condition   : {weather}"
            )

            result.config(text=report)

        else:
            result.config(text="City not found!")

    except urllib.error.HTTPError as e:
        result.config(text=f"HTTP Error: {e.code}")

    except urllib.error.URLError as e:
        result.config(text=f"Network Error: {e.reason}")

    except Exception as e:
        result.config(text=f"Error: {e}")

# Main Window
root = tk.Tk()
root.title("Weather App")
root.geometry("500x400")

title = tk.Label(
    root,
    text="Weather Forecast Application",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=10)

search_button = tk.Button(
    root,
    text="Get Weather",
    command=get_weather,
    font=("Arial", 11)
)
search_button.pack(pady=10)

result = tk.Label(
    root,
    text="Enter a city name and click Get Weather",
    font=("Arial", 11),
    justify="left"
)
result.pack(pady=20)

root.mainloop()