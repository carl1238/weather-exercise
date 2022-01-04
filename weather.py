# Weather Exercise
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
            f"The temperature at HK is {self.temperature}. A {self.wind_speed} wind at {self.wind_direction} is "
            f"hitting this place.")


location = input("Where are you? : ")
today_temperature = input("Input Current Temperature (deg C): ")
today_wind_speed = input("Input Current Wind Speed (km/h): ")
today_wind_direction = input("Input Current Wind Direction (E/S/W/N/NE/SE/NW/SW): ")

today_weather = Weather(today_temperature, today_wind_speed, today_wind_direction)
today_weather.report()
