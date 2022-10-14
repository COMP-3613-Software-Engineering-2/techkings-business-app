import flask_login
from flask_jwt import JWT
from App.models import admin


def authenticate(username, password):
    admin_user = admin.query.filter_by(username=username).first()
    if admin_user and admin_user.check_password(password):
        return admin_user
    return None

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return admin.query.get(payload['identity'])

def login_admin_user(admin_user, remember):
    return flask_login.login_admin_user(admin_user, remember=remember)


def logout_admin_user():
    flask_login.logout_admin_user()

def setup_jwt(app):
    return JWT(app, authenticate, identity)