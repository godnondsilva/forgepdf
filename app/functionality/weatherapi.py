import json, requests 

# function to call the API from the user defined API and return the response
def getWeatherData():
    # trying to get the response from the api and storing it in the weatherData variable
    try:
        data = requests.get('http://localhost:5000/weather')
        # storing the the json form of the response's text 
        weatherData = json.loads(data.text)
    # if there was an error while retrieving the data, we return an the following dictionary
    except:
        data = json.dumps({"error": "Could not connect to the server, please run the server first"})
        weatherData = json.loads(data)
    # storing the weather data in a JSON file
    json.dump(weatherData, open('weather.json', 'w'))

# function to load the weather data from the JSON file
def loadWeatherData():
    # opening the weather.json file in write mode
    file = open('weather.json', 'r')
    # loading the weather data from the JSON file
    weatherData = json.load(file)
    # returning the weatherData variables
    return weatherData
