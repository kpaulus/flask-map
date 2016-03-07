from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

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


@app.route('/new', methods=['POST'])
def new():

    point_doc = {
        'lat': request.form['lat'],
        'lon': request.form['lon']
    }
    db.mapdb.insert_one(point_doc)

    return redirect(url_for('map'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
