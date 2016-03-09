from flask import Flask, redirect, url_for, request, render_template, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient(
    'mongo',
    27017)
db = client.mapdb


@app.route('/')
def map():

    _points = db.mapdb.find()
    for point in _points:
        points.append('lat': point.lat, 'lon': point.lon)

    return render_template('map.html', points=points)

@app.route('/locations', methods=['GET'])
def get_locations():

    _points = db.mapdb.find()
    for point in _points:
        points.append('lat': point.lat, 'lon': point.lon)

    return jsonify({ 'points': points })
    
@app.route('/location', methods=['POST'])
def location():

    point_doc = {
        'user': request.json['user'],
        'lat': request.json['lat'],
        'lon': request.json['lon'],
        'timestamp': str(datetime.utcnow())
    }

    # testing on the map
    db.mapdb.insert_one(point_doc)

    #return redirect(url_for('map'))
    return str(point_doc), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
