from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asñldkfSOEWEKlaskñ2309234ñli092ka94a4'

    return app

