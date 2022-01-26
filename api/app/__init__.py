import os
from flask import Flask,current_app

from app.libs.users_manager import UsersManager
# from app.assets import app_css, app_js, vendor_css, vendor_js

from flask_mongoengine import MongoEngine

basedir = os.path.abspath(os.path.dirname(__file__))

db = MongoEngine()


def create_app(config_name):
    app = Flask(__name__)
    # TODO: make config read from yaml
    app.config.update(
        MONGODB_SETTINGS = 
        {
            "db": 'mydb',
            # "host": "localhost",
            'connect': False,
            'alias':'default'
        },
        JSP_FQDN = "https://jsonplaceholder.typicode.com",
        JSP_CONNECT_TIMEOUT = 5,
    )
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api_v1 as api_blueprint_v1

    app.register_blueprint(api_blueprint_v1, url_prefix='/api/v1')


    @app.route('/healthz')
    def get_healthz():
        return "OK", 200


    @app.errorhandler(500) #side-wide 500 handler
    def internal_error(error):
        return "internal error", 500

    @app.errorhandler(404)  #side-wide 404 handler
    def notfound_error(error):
        return "request dest not found", 404



    return app
