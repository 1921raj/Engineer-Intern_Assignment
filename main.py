import requests
import datetime

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(url)
    data = response.json()
    return data

def get_temperature(data, date_time):
    for item in data["list"]:
        if item["dt_txt"] == date_time:
            temperature = item["main"]["temp"]
            return temperature
    return None

def get_wind_speed(data, date_time):
    for item in data["list"]:
        if item["dt_txt"] == date_time:
            wind_speed = item["wind"]["speed"]
            return wind_speed
    return None

def get_pressure(data, date_time):
    for item in data["list"]:
        if item["dt_txt"] == date_time:
            pressure = item["main"]["pressure"]
            return pressure
    return None

def main():
    data = get_weather_data()
    while True:
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        date_time = input("Enter date and time (yyyy-mm-dd hh:mm:ss): ")
        if choice == "1":
            temperature = get_temperature(data, date_time)
            if temperature is not None:
                print(f"Temperature: {temperature} K")
            else:
                print("No data found for the given date and time.")
        elif choice == "2":
            wind_speed = get_wind_speed(data, date_time)
            if wind_speed is not None:
                print(f"Wind Speed: {wind_speed} meter/sec")
            else:
                print("No data found for the given date and time.")
        elif choice == "3":
            pressure = get_pressure(data, date_time)
            if pressure is not None:
                print(f"Pressure: {pressure} hPa")
            else:
                print("No data found for the given date and time.")

if __name__ == "__main__":
    main()
