import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def get_database_uri():
    return f"sqlite:///{os.path.join(basedir, '../app.db')}"