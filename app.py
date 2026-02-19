from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from routes import register_routes

app = Flask(__name__)

register_routes(app)

if __name__=='__main__':
    app.run(debug=True)