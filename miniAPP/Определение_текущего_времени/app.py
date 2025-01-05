# Определение текущего времени в любой стране

import requests

API_URL = "http://worldtimeapi.org/api/timezone"


def get_timezones():
    """Получает список всех доступных часовых поясов."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None


def get_time_by_timezone(timezone):
    """Получает текущее время для указанного часового пояса."""
    try:
        response = requests.get(f"{API_URL}/{timezone}")
        response.raise_for_status()
        data = response.json()
        return data.get("datetime")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None


if __name__ == "__main__":
    print("Программа для получения текущего времени по часовому поясу.")
    print("Загрузка доступных часовых поясов...")
    timezones = get_timezones()

    if timezones:
        print("\nПример часовых поясов:")
        print(", ".join(timezones[:10]) + ", ...")

        timezone = input("\nВведите желаемый часовой пояс (например, Europe/Moscow): ").strip()
        if timezone in timezones:
            current_time = get_time_by_timezone(timezone)
            if current_time:
                print(f"Текущее время в {timezone}: {current_time}")
        else:
            print("Неверный часовой пояс. Проверьте правильность ввода.")
