from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name, password, email):
        self.name = name
        self.set_password(password)
        self.email = email

    def toJSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

