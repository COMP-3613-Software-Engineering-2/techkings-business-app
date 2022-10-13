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
    