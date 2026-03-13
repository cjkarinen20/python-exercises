from weatherDataGen import get_random_weather_data

def get_average_temperature(weather_data):
    tempCount = 0
    sum = 0
    for index, dict in enumerate(weather_data):
        sum += dict['temp']
        tempCount += 1
        
    avgTemp = sum / tempCount
    return round(avgTemp, 2)

if __name__ == "__main__":
    weatherDataList = []
    for i in range(100): # Run the function 100 times
        randomWeatherData = get_random_weather_data()
        weatherDataList.append(randomWeatherData) # Add the weather data to the result list
    print(get_average_temperature(weatherDataList))