from flask import request, jsonify
from app import app, db
from app.models import User
import json
import os
import json
import requests

# Route to register a new user
@app.route('/api/register', methods=['POST'])
def register():
    try:
        # getting the data from the request
        data = request.get_json()
        if data is None:
            return jsonify
            (
                {
                    'status': 'error',
                    'message': 'No input data provided'
                }
            ), 400
        # checking if the user already exists
        user = User.query.filter_by(email=data['email']).first()
        if user:
            return jsonify
            (
                {
                    'status': 'error',
                    'message': 'User already exists'
                }
            ), 400
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
        return jsonify
        (
            {
                'status': 'success',
                'message': 'User created successfully.'
            }
        ), 200
    except Exception as e:
        return jsonify
        (
            {
                'status': 'error',
                'message': 'An error occurred. Please try again.'
            }
        ), 500

# Route to login a user
@app.route('/api/login', methods=['POST'])
def login():
    try:
        # getting the data from the request
        data = request.get_json()
        if data is None:
            return {
                'status': 'error',
                'message': 'No input data provided'
            }, 400
        # getting the user from the database
        user = User.query.filter_by(email=data['email']).first()
        # checking if the user exists
        if not user:
            return {
                "status": 'error',
                "message": 'User does not exist'
            }, 200
        # checking if the password is correct
        if user.password != data['password']:
            return {
                "status": 'error',
                'message': 'Incorrect password.'
            }, 200
        return {
            "status": 'success',
            'message': 'User logged in successfully.',
            'payload': {
                'name': user.name,
                'email': user.email
            }
        }, 200
            
    except:
        return {
            "status": 'error',
            'message': 'An error occurred. Please try again.'
        }, 500
        

# Route to get the weather data
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
        return {
            'status': 'success',
            'message': 'Weather data fetched successfully.',
            'payload': weather_data
        }, 200
    except:
        return {
            'error': 'An error has occurred.'
        }, 500
    # returning the data in json format

# Route to get the weather data
@app.route('/api/thought', methods=['GET'])
def get_thought():
    data = []
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
        return {
            'status': 'success',
            'message': 'Thought of the day fetched successfully.',
            'payload': data
        }, 200
    except:
        return {
            'error': 'An error has occurred.'
        }, 500
    # returning the data in json format
