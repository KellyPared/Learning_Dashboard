from flask import Flask, render_template, redirect, jsonify
from unesco_data import data, schools

import plotly.graph_objs as go
import json
from pymongo import MongoClient
import folium
import pandas as pd

app = Flask(__name__)

# Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['students']
# collection = db['student_data']

@app.route('/')
def index():
    # Query student data from MongoDB
    # students = {}
    # for doc in collection.find():
    #     student = {
    #         'age': doc['age'],
    #         'siblings': doc['siblings'],
    #         'interests': doc['interests'],
    #         'gpa': doc['gpa']
    #     }

    #USE FAKE DATABASE FOR NOW
    # Replace the MongoDB connection code with a dictionary
    students = {
        'Jane Doe': {'age': 13, 'siblings': 3, 'interests': 'dance', 'gpa': 3.7},
        'John Smith': {'age': 15, 'siblings': 1, 'interests': 'soccer', 'gpa': 3.5},
        'Samantha Johnson': {'age': 14, 'siblings': 2, 'interests': 'music', 'gpa': 4.0},
        'Adam Lee': {'age': 13, 'siblings': 0, 'interests': 'science', 'gpa': 3.2},
        'Emily Kim': {'age': 15, 'siblings': 2, 'interests': 'art', 'gpa': 3.9}
    }

    # students[doc['name']] = student

    # Create a bar graph of student GPAs
    graph_data = [go.Bar(
                x=list(students.keys()),
                y=[student['gpa'] for student in students.values()]
            ).to_plotly_json()]

    # Create a dropdown menu of student names
    dropdown_menu = [{'label': name, 'value': name} for name in students.keys()]

    # Render the template with the graph and dropdown menu
    return render_template('index.html', graph_data=json.dumps(graph_data), dropdown_menu=dropdown_menu)

@app.route('/schools_map')
def schools_map():
    # Get data and create map
    data = data
    # map_html = get_map(schools_data)
    # Create a map of schools
    map_data = {
            'type': 'scattergeo',
        'locationmode': 'ISO-3',
        'lat': data['lat'],
        'lon': data['lon'],
        'text': data['name'],
        'mode': 'markers',
        'marker': {
            'color': data['color'],
            'size': data['size'],
            'opacity': 0.7,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Number of Students'}
        },
    }

    layout = {'title': 'UNESCO Schools Map'}

    # Render the template with the map and dropdown menu
    return render_template('schools_map.html', map_data=map_data, layout=layout, dropdown_menu=request.args.get('dropdown_menu'))



if __name__ == '__main__':
    app.run(debug=True)