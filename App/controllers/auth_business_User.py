import flask_login
from flask_jwt import JWT
from App.models import business_User


def authenticate(name, password):
    buss_user = buss_user.query.filter_by(name=name).first()
    if buss_user and buss_user.check_password(password):
        return buss_user
    return None

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return business_User.query.get(payload['identity'])

def login_buss_user(buss_user, remember):
    return flask_login.login_buss_user(buss_user, remember=remember)


def logout_buss_user():
    flask_login.logout_buss_user()

def setup_jwt(app):
    return JWT(app, authenticate, identity)