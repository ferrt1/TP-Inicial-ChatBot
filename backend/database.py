from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email =  db.Column(db.String(45), unique=True, nullable=False)
    user_id = db.Column(db.LargeBinary, unique=True, nullable=False)
    credential_id = db.Column(db.LargeBinary, unique=True)
    public_key = db.Column(db.LargeBinary, unique=True)
    sign_count = db.Column(db.Integer)