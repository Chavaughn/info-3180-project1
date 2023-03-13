from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate
import os
# import flask migrate here

app = Flask(__name__)
app.config.from_object(Config)
app.config['PROPERTIES_FOLDER'] = os.path.abspath('./properties/')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Initialize database with property types
from app import models_init
with app.app_context():
    models_init.init_property_types(db)
    models_init.intit_photos(db)
    models_init.init_properties(db)

# Import views after database initialization
from app import views
