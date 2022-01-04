# Weather Exercise
from typing import Any


class Weather:
    def __init__(self, temperature, wind_speed, wind_direction):
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

    def direction_rename(self):
        if self.wind_direction == 'E':
            return "East"
        elif self.wind_direction == 'W':
            return "West"
        elif self.wind_direction == 'N':
            return "North"
        elif self.wind_direction == 'S':
            return "South"
        elif self.wind_direction == 'SE':
            return "South East"
        elif self.wind_direction == 'SW':
            return "South West"
        elif self.wind_direction == 'NE':
            return "North East"
        elif self.wind_direction == 'NW':
            return "North West"
        else:
            return 1

    def report(self):
        print(
            f"The temperature at HK is {self.temperature} deg C. The {self.direction_rename()} wind at {self.wind_speed}"
            f"km/h is hitting this place.")


class VerbalWeather(Weather):

    def check_temperature(self):
        dummy_temp = int(self.temperature)
        if dummy_temp >= 20 & dummy_temp < 40:
            return 'Warm'
        elif dummy_temp >= 40:
            return "Hot"
        elif dummy_temp < 20 & dummy_temp > 10:
            return "Cool"
        elif dummy_temp <= 10 & dummy_temp > 5:
            return "Cold"
        elif dummy_temp <= 5:
            return "Freezing"

    def check_wind_speed(self):
        dummy_speed = int(self.wind_speed)
        if dummy_speed >= 30:
            return 'Windy'
        elif dummy_speed < 30:
            return 'Comfortable'

    def report(self):
        print(
            f"Today is {self.check_temperature()}. The {self.direction_rename()} wind is {self.check_wind_speed()}.")


# location = input("Where are you? : ")
today_temperature = input("Input Current Temperature (deg C): ")
today_wind_speed = input("Input Current Wind Speed (km/h): ")
today_wind_direction = input("Input Current Wind Direction (E/S/W/N/NE/SE/NW/SW): ")

print("Detail Report")
today_weather = Weather(today_temperature, today_wind_speed, today_wind_direction)
today_weather.report()

print("Verbal Report")
today_v_weather = VerbalWeather(today_temperature, today_wind_speed, today_wind_direction)
today_v_weather.report()
