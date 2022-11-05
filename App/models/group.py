from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    groupname =  db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, groupname, password):
        self.groupname = groupname
        self.set_password(password)

    def toJSON(self):
        return{
            'id': self.id,
            'groupname': self.groupname,
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

