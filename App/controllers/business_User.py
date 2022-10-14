from App.models import business_User
from App.database import db

def generate_session(session_id,groupNumber ):
    newsession = business_User(session_id=session_id, groupNumber=groupNumber)
    db.session.add(newsession)
    db.session.commit()
    return newsession

def get_sessions_by_groupNumber(groupNumber):
    return business_User.query.filter_by(groupNumber=groupNumber).first()

def get_session(session_id):
    return business_User.query.get(session_id)

def get_all_sessions():
    return business_User.query.all()

def get_all_business_Users_json():
    user = business_User.query.all()
    if not user:
        return []
    user = [business_User.toJSON() for business_User in user]
    return user

def update_business_User(session_id, groupNumber):
    user = get_sessions_by_groupNumber(groupNumber)
    if user:
        user.groupNumber=groupNumber
        db.session.add(user)
        return db.session.commit()
    return None
    