from flask import Flask, request
import json, requests

app = Flask(__name__)

# function to convert kelvin to celsius
def convertToCelsius(kelvin):
    return round(kelvin - 273.15, 2)

# api route to get the weather data
@app.route('/weather' , methods = ['GET'])
def getWeather():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=mangalore&appid=f5990901916de44b03db0a2d1c42140d'
    # getting the content of the request
    response = requests.get(url)
    # throwing exception in case of api error
    response.raise_for_status()
    # converting the response from json to python dictionary
    weatherData = json.loads(response.text)
    # store all the data to send in a dictionary
    dataToSend = {
        'temp': convertToCelsius(weatherData['main']['temp']),
        'feels_like': convertToCelsius(weatherData['main']['feels_like']),
        'humidity': weatherData['main']['humidity'],
        'description': weatherData['weather'][0]['description'],
        'wind_speed': weatherData['wind']['speed']
    }
    # returning the data in json format
    return json.dumps(dataToSend)

@app.route('/emailvalidate' , methods = ['GET'])
def getEmailValidate():
    # getting the email from the request argument
    email = request.args.get('email')
    # passing the email to the api to validate
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email}
    )
    # getting the data from the response
    status = response.json()['status']
    # checking if the status is valid
    if status == "valid":
        return {"response": True}
    # checking if the status is invalid
    elif status == "invalid":
        return {"error": "Please enter a valid email address!"}
    # all other cases
    else:
        return {"error": "Please enter a valid email address!"}

if __name__ == "__main__":
    app.run(debug=True)