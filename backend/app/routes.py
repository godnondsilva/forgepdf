from flask import request, jsonify, send_file
from app import app, db
from app.models import User
import json
import os
import json, requests

# route to register a new user
@app.route('/api/register', methods=['POST'])
def register():
    # getting the data from the request
    data = request.get_json()
    # creating a new user
    user = User(
        name=data['name'],
        email=data['email'],
        password=data['password']
    )
    # saving the user to the database
    db.session.add(user)
    db.session.commit()
    # returning the data in json format
    return jsonify({'message': 'User created successfully.'})

# route to login a user
@app.route('/api/login', methods=['POST'])
def login():
    # getting the data from the request
    data = request.get_json()
    # getting the user from the database
    user = User.query.filter_by(email=data['email']).first()
    # checking if the user exists
    if user:
        # checking if the password is correct
        if user.password == data['password']:
            # returning the data in json format
            return jsonify({'message': 'User logged in successfully.'})
        else:
            # returning the data in json format
            return jsonify({'error': 'Incorrect password.'})
    else:
        # returning the data in json format
        return jsonify({'error': 'User does not exist.'})

# route to get the weather data
@app.route('/api/weather/<location>', methods=['GET'])
def get_weather(location):
    data = {}
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={app.config["WEATHER_API_KEY"]}'
        # getting the content of the request
        response = requests.get(url)
        # throwing exception in case of api error
        response.raise_for_status()
        # converting the response from json to python dictionary
        weather_data = json.loads(response.text)
        # store all the data to send in a dictionary
        data = weather_data
    except:
        data = {
            'error': 'An error has occurred.'
        }
    # returning the data in json format
    return data

# route to get the thought of the day
@app.route('/api/thought', methods=['GET'])
def get_thought():
    data=[]
    try:
        url = 'https://zenquotes.io/api/today'
        # getting the content of the request
        response = requests.get(url)
        # throwing exception in case of api error
        response.raise_for_status()
        # converting the response from json to python dictionary
        thought_data = json.loads(response.text)
        # store all the data to send in a dictionary
        data = thought_data[0]['q']
    except:
        data = {
            'error': 'An error has occurred.'
        }
    # returning the data in json format
    return data

