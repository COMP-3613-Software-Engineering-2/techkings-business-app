from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Business_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    session_id = db.Column(db.Integer)
    name =  db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    groupNumber = db.Column(db.Integer)
    
    

    def __init__(self, name, password, email):
        self. customer_id = customer_id
        self.session_id = session_id
        self.name = name
        self.set_password(password)
        self.email = email
        self.groupNumber = groupNumber

    def toJSON(self):
        return{
            'id': self.id,
            'customer_id': self.customer_id,
            'session_id': self.session_id,
            'name': self.name,
            'email': self.email,
            'groupNumber': self.groupNumber
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

