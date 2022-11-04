from App.models import ICT_team
from App.database import db

def create_user(username, password):
    newuser = ICT_team(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return ICT_team.query.filter_by(username=username).first()

def get_user(id):
    return ICT_team.query.get(id)

def get_all_users():
    return ICT_team.query.all()

def get_all_users_json():
    users = ICT_team.query.all()
    if not users:
        return []
    users = [ICT_team.toJSON() for ICT_team in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

#used for group
def create_group(groupname, password):
    newgroup = ICT_team(groupname=groupname, password=password)
    db.session.add(newgroup)
    db.session.commit()
    return newgroup

def get_user_by_groupname(groupname):
    return ICT_team.query.filter_by(groupname=groupname).first()

def get_group(id):
    return ICT_team.query.get(id)

def get_all_groups():
    return ICT_team.query.all()

def get_all_groups_json():
    groups = ICT_team.query.all()
    if not groups:
        return []
    groups = [ICT_team.toJSON() for ICT_team in groups]
    return groups

def update_group(id, groupname):
    group = get_user(id)
    if group:
        group.groupname = groupname
        db.session.add(group)
        return db.session.commit()
    return None