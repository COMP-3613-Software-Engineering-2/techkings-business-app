import flask_login
from flask_jwt import JWT
from App.models import customer


def authenticate(name, password):
    cus = cus.query.filter_by(name=name).first()
    if cus and cus.check_password(password):
        return cus
    return None

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return customer.query.get(payload['identity'])

def login_customer(cus, remember):
    return flask_login.login_customer(cus, remember=remember)


def logout_customer():
    flask_login.logout_customer()

def setup_jwt(app):
    return JWT(app, authenticate, identity)