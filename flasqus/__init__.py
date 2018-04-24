from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


RECAPTCHA_PUBLIC_KEY = app.config.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = app.config.get('RECAPTCHA_PRIVATE_KEY')

import flasqus.views
