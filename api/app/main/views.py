from flask import Blueprint, redirect, render_template, url_for,make_response,jsonify,current_app

# from app.models import EditableHTML

main = Blueprint('main', __name__)


@main.route('/')
def index():
    # return render_template('main/index.html')
    return "", 200