from flask import Blueprint

auth = Blueprint('auth', __name__)

@views.route('/auth')
def home():
    return "<h1>Test</h1>"