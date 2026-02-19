from flask_sqlalchemy import SQLAlchemy
from flask import render_template, redirect, url_for



def register_routes(app):
    
    @app.route("/")
    def index():
        return render_template('index.html')
    

    @app.route('/shows')
    def shows():
        return render_template('shows.html')