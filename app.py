from flask import Flask

flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return 'Hello world'

@flask_app.route('/admin/')
def admin():
    return 'Hello admin'


@flask_app.route('/admin/<string:name>/')
def admin_name(name):
    return 'Hello {}'.format(name)
