from App.models import group
from App.database import db

def sign_up(name, password):
    newgroup = group(name=name, password=password)
    db.session.add(newgroup)
    db.session.commit()
    return newgroup

def get_groups_by_name(name):
    return group.query.filter_by(name=name).first()

def get_group(id):
    return group.query.get(id)

def get_all_groups():
    return group.query.all()

def get_all_groups_json():
    grp = group.query.all()
    if not grp:
        return []
    grp = [group.toJSON() for group in grp]
    return grp

def update_group(id, name):
    grp = get_group(id)
    if grp:
        grp.name = name
        db.session.add(grp)
        return db.session.commit()
    return None
    