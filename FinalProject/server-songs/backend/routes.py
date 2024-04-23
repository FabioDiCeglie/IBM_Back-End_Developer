from . import app
import os
import json
import pymongo
from flask import jsonify, request, make_response, abort, url_for
from pymongo import MongoClient
from bson import json_util
from pymongo.errors import OperationFailure
from pymongo.results import InsertOneResult
from bson.objectid import ObjectId
import sys


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "songs.json")
songs_list: list = json.load(open(json_url))

# client = MongoClient(
#     f"mongodb://{app.config['MONGO_USERNAME']}:{app.config['MONGO_PASSWORD']}@localhost")
mongodb_service = os.environ.get('MONGODB_SERVICE')
mongodb_username = os.environ.get('MONGODB_USERNAME')
mongodb_password = os.environ.get('MONGODB_PASSWORD')
mongodb_port = os.environ.get('MONGODB_PORT')

print(f'The value of MONGODB_SERVICE is: {mongodb_service}')

if mongodb_service == None:
    app.logger.error('Missing MongoDB server in the MONGODB_SERVICE variable')
    # abort(500, 'Missing MongoDB server in the MONGODB_SERVICE variable')
    sys.exit(1)

if mongodb_username and mongodb_password:
    url = f"mongodb+srv://{mongodb_username}:{mongodb_password}@{mongodb_service}"
else:
    url = f"mongodb+srv://{mongodb_service}"


print(f"connecting to url: {url}")

try:
    client = MongoClient(url)
except OperationFailure as e:
    app.logger.error(f"Authentication error: {str(e)}")

db = client.songs
db.songs.drop()
db.songs.insert_many(songs_list)

def parse_json(data):
    return json.loads(json_util.dumps(data))

######################################################################
# INSERT CODE HERE
######################################################################
@app.route("/health", methods=["GET"])
def check():
    return {"status": "OK"}, 200

@app.route("/count")
def count():
    count = len(songs_list)
    return {"count": count}, 200

@app.route("/songs")
def get_songs():
    songs_cursor = db.songs.find({})
    return {"songs": json.loads(json_util.dumps(songs_cursor))}, 200

@app.route("/songs/<int:id>")
def get_songs_by_id(id):
    songs_cursor = db.songs.find_one({"id": id})
    return {"songs": json.loads(json_util.dumps(songs_cursor))}, 200

@app.route("/song", methods=["POST"])
def create_song():
    song_in = request.json

    # if the id is already there, return 303 with the URL for the resource
    song = db.songs.find_one({"id": song_in["id"]})
    if song:
        return {
            "Message": f"song with id {song_in['id']} already present"
        }, 302

    db.songs.insert_one(song_in)
    return {"inserted song": parse_json(song_in)}, 201

@app.route("/song", methods=["PUT"])
def create_song():
    song_in = request.json
    
    # if the id is already there, return 303 with the URL for the resource
    song = db.songs.find_one({"id": song_in["id"]})
    if song:
        return {
            "Message": f"song with id {song_in['id']} already present"
        }, 302

    db.songs.insert_one(song_in)
    return {"inserted song": parse_json(song_in)}, 201