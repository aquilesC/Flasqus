from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


RECAPTCHA_PUBLIC_KEY = app.config.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = app.config.get('RECAPTCHA_PRIVATE_KEY')

import flasqus.views
