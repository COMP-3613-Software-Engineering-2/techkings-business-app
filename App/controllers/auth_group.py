import flask_login
from flask_jwt import JWT
from App.models import group


def authenticate(name, password):
    grp = grp.query.filter_by(name=name).first()
    if grp and grp.check_password(password):
        return grp
    return None

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return group.query.get(payload['identity'])

def login_group(grp, remember):
    return flask_login.login_group(grp, remember=remember)


def logout_group():
    flask_login.logout_group()

def setup_jwt(app):
    return JWT(app, authenticate, identity)