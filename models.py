from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Admins(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    pw_hash = db.Column(db.String(50), nullable=False)

class Shows(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    venue = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    img_filename = db.Column(db.String(50), nullable=True)
    ticket_link = db.Column(db.String(100), nullable=True)

class Merch(db.Model):
    __tablename = 'merch'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(100), nullable=False)
