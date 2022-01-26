#libs

from base64 import b64encode
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from datetime import datetime
import json

from flask import abort, current_app, jsonify, request,url_for,g
from werkzeug.datastructures import MultiDict
from app.libs.users_manager import UsersManager
from . import api_v1



@api_v1.route('/usersync', methods=["POST"])
def sync_users():
    """
     POST create a sync for users
    ---
    tags:
      - user
    # parameters:
    #   - in: header
    #     name: Authorization
    #     type: string
    #     required: true"
    responses:
      201:
        description: ok
    """
    UsersManager.sync_users_from_source()
    return jsonify({"result":"ok"}), 200


@api_v1.route('/users', methods=["GET"])
def get_users():
    """
     Get users List with basic info
    ---
    tags:
      - user
    # parameters:
    #   - in: header
    #     name: Authorization
    #     type: string
    #     required: true"
    responses:
      200:
        description: ok
    """
    um = UsersManager()
    users = um.get_users_list()
    return jsonify(users), 200


@api_v1.route('/user/<userid>', methods=["GET"])
def get_users_destail(userid):
    """
     Get user's detail inforamtion including posts and todos
    ---
    tags:
      - user
    parameters:
      - in: path
        name: userid
        type: string
        required: true"
    responses:
      200:
        description: ok
    """
    um = UsersManager()
    u = um.get_user(userid)
    if u is None:
      return jsonify({"message":"user not found"}), 404
    return jsonify(u), 200