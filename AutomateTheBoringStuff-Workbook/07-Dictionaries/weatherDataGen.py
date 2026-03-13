import random

def get_random_weather_data():
    randomWeather = {'temp': 0, 'feels_like': 0, 'humidity': 0, 'pressure': 0}
    
    randomWeather['temp'] = random.uniform(-50, 50) # Temp is a random float from -50 to 50
    randomWeather['feels_like'] = random.uniform(randomWeather['temp'] - 10, randomWeather['temp'] + 10)
    # Feels-like is a random float within 10 degrees of temp
    randomWeather['humidity'] = random.randint(0, 100) # Humidity is a random int between 0 and 100
    randomWeather['pressure'] = random.randint(990, 1010) # Pressure is a random int between 990 and 1010
    
    return randomWeather

if __name__ == "__main__":
    weatherDataList = []
    for i in range(100): # Run the function 100 times
        randomWeatherData = get_random_weather_data()
        weatherDataList.append(randomWeatherData) # Add the weather data to the result list
        print(f"{randomWeatherData}\n") 
    
