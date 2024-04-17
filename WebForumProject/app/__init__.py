# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IhrGeheimerSchlüssel'
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))

# Verschieben Sie den Import von 'routes' an das Ende der Datei
# und stellen Sie sicher, dass 'routes' nicht 'app' importiert,
# bevor 'app' vollständig initialisiert ist.

# Ihr bisheriger Code ...

# Importieren Sie 'routes' am Ende der Datei
from app import routes
