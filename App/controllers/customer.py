from App.models import customer
from App.database import db

def sign_up(name, password):
    newuser = customer(name=name, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_customers_by_name(name):
    return customer.query.filter_by(name=name).first()

def get_customer(id):
    return customer.query.get(id)

def get_all_customers():
    return customer.query.all()

def get_all_customers_json():
    cus = customer.query.all()
    if not cus:
        return []
    cus = [customer.toJSON() for customer in cus]
    return cus

def update_customer(id, name):
    cus = get_customer(id)
    if cus:
        cus.name = name
        db.session.add(cus)
        return db.session.commit()
    return None
    