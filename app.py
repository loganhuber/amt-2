from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from routes import register_routes
from routes_admin import register_admin_routes
from models import db

app = Flask(__name__)
admin = Admin()

app.config['SQLITE_DATABASE_URI'] = 'sqlite3:///db.sqlite3'
app.config['SECRET_KEY'] = 'my_secret'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
admin.init_app(app)

register_routes(app)
register_admin_routes(app)

if __name__=='__main__':
    app.run(debug=True)