from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    try:
        if data:
            return jsonify(data), 200
    except:
        return {"message": "Pictures not found"}, 404

######################################################################
# GET A PICTURE
######################################################################
def find(arr , id):
    for x in arr:
        if x["id"] == id:
            return x

@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    try:
        picture_by_id = find(data, id)
        if picture_by_id:
            return jsonify(picture_by_id), 200
        else:
            return jsonify({"message": f"Picture with ID {id} not found"}), 404
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    try:
        new_picture = request.json
        picture_by_id = find(data, new_picture['id'])
        if picture_by_id is None:
            data.append(new_picture)
            return jsonify(new_picture), 201
        else:
            return jsonify({"Message": f"picture with id {new_picture['id']} already present"}), 302 
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    try:
        updated_picture = request.json
        if updated_picture:
            for idx, item in enumerate(data):
                if id == item['id']:
                    data[idx] = updated_picture
                    return jsonify(data), 200
        else:
            return jsonify({"message": "picture not found"}), 404
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    try: 
        for picture in data:
            if picture["id"] == id:
                data.remove(picture)
                return "", 204 
        return {"message": "picture not found"}, 404
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500
