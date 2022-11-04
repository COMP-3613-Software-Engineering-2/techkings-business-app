from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

@app.route
def get_migrate(app):
    return Migrate(app, db)

@app.route
def create_db(app):
    db.init_app(app)
    db.create_all(app=app)

@app.route    
def init_db(app):
    db.init_app(app)