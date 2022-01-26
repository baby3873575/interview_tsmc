from flask import Blueprint
api_v1 = Blueprint('api.v1', __name__)
from app.api.v1.user_api import *