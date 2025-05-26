import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from typing import Dict, Any, List, Optional
from datetime import datetime


class WeatherApp:
    """GUI application to display weather forecast for Russian cities."""

    def __init__(self, root: tk.Tk):
        """
        Initialize the weather application.

        Args:
            root: The tkinter root window
        """
        self.root = root
        self.root.title("Прогноз погоды для городов России")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # API key for OpenWeatherMap (you should replace with your own)
        self.api_key = "8e39660a6f1480149a4ade2d3b2c06c8"  # Free test key

        # List of major Russian cities
        self.cities = [
            "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург",
            "Казань", "Нижний Новгород", "Челябинск", "Самара",
            "Омск", "Ростов-на-Дону", "Уфа", "Красноярск",
            "Воронеж", "Пермь", "Волгоград"
        ]

        self.create_widgets()

    def create_widgets(self) -> None:
        """Create and arrange UI widgets."""
        # Frame for city selection
        select_frame = ttk.LabelFrame(self.root, text="Выберите город")
        select_frame.pack(padx=20, pady=20, fill="x")

        # City dropdown
        ttk.Label(select_frame, text="Город:").grid(row=0, column=0, padx=5, pady=5)
        self.city_var = tk.StringVar()
        city_combo = ttk.Combobox(select_frame, textvariable=self.city_var, values=self.cities, state="readonly")
        city_combo.grid(row=0, column=1, padx=5, pady=5)
        city_combo.bind("<<ComboboxSelected>>", self.get_weather)

        # Frame for weather display
        self.weather_frame = ttk.LabelFrame(self.root, text="Прогноз погоды")
        self.weather_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Weather info text
        self.weather_text = tk.Text(self.weather_frame, wrap=tk.WORD, height=15, width=60)
        self.weather_text.pack(padx=10, pady=10, fill="both", expand=True)
        self.weather_text.config(state=tk.DISABLED)

    def get_weather(self, event: Optional[tk.Event] = None) -> None:
        """
        Fetch and display weather for the selected city.

        Args:
            event: The event that triggered this function (optional)
        """
        city = self.city_var.get()
        if not city:
            return

        try:
            # API call to OpenWeatherMap
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city},ru&appid={self.api_key}&units=metric&lang=ru"
            response = requests.get(url)
            data = response.json()

            if response.status_code != 200:
                messagebox.showerror("Ошибка",
                                     f"Не удалось получить данные: {data.get('message', 'Неизвестная ошибка')}")
                return

            # Extract weather information
            weather_info = self.format_weather_data(data)

            # Update the text widget with weather information
            self.weather_text.config(state=tk.NORMAL)
            self.weather_text.delete(1.0, tk.END)
            self.weather_text.insert(tk.END, weather_info)
            self.weather_text.config(state=tk.DISABLED)

        except requests.RequestException as e:
            messagebox.showerror("Ошибка сети", f"Ошибка при соединении с сервером: {str(e)}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def format_weather_data(self, data: Dict[str, Any]) -> str:
        """
        Format the weather data into a readable string.

        Args:
            data: The JSON data from the weather API

        Returns:
            Formatted weather information as a string
        """
        city_name = data["name"]
        weather_desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = int(data["main"]["pressure"] * 0.75)  # Convert hPa to mmHg
        wind_speed = data["wind"]["speed"]
        wind_dir = self.get_wind_direction(data["wind"]["deg"])
        clouds = data["clouds"]["all"]

        # Get current time from timestamp
        timezone_offset = data["timezone"]
        local_time = datetime.utcfromtimestamp(data["dt"] + timezone_offset).strftime('%H:%M:%S %d.%m.%Y')

        # Sunrise and sunset times
        sunrise = datetime.utcfromtimestamp(data["sys"]["sunrise"] + timezone_offset).strftime('%H:%M:%S')
        sunset = datetime.utcfromtimestamp(data["sys"]["sunset"] + timezone_offset).strftime('%H:%M:%S')

        # Format output
        weather_info = f"""
        Погода в городе: {city_name}
        Местное время: {local_time}

        Погодные условия: {weather_desc}
        Температура: {temp:.1f}°C
        Ощущается как: {feels_like:.1f}°C

        Влажность: {humidity}%
        Давление: {pressure} мм рт.ст.
        Облачность: {clouds}%

        Ветер: {wind_speed} м/с, {wind_dir}

        Восход солнца: {sunrise}
        Закат солнца: {sunset}
        """

        return weather_info

    def get_wind_direction(self, degrees: float) -> str:
        """
        Convert wind direction in degrees to cardinal direction.

        Args:
            degrees: Wind direction in degrees

        Returns:
            Cardinal direction as a string
        """
        directions = ["северный", "северо-восточный", "восточный", "юго-восточный",
                      "южный", "юго-западный", "западный", "северо-западный"]
        index = round(degrees / 45) % 8
        return directions[index]


def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()