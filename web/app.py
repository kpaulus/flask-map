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
    points = [point for point in _points]

    return render_template('map.html', points=points)

@app.route('/points', methods=['GET'])
def get_points():
    
    _points = db.mapdb.find()
    points = [point for point in _points]

    return jsonify({'points': points})

@app.route('/points', methods=['POST'])
def insert_points():

    if not request.json or not 'pid' in request.json:
        abort(400)

    point_doc = {
        'pid': int(request.json['pid']),
        'pos': [float(request.json['lat']), 
                float(request.json['lon'])],
        'timestamp': datetime.now()
    }
    db.mapdb.insert_one(point_doc)

    return jsonify({'point': point_doc}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
