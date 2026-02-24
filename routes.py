from flask_sqlalchemy import SQLAlchemy
from flask import render_template, redirect, url_for
from models import Shows, Merch
from datetime import datetime



def register_routes(app):
    
    @app.route("/")
    def index():
        return render_template('public/index.html')
    

    @app.route('/shows')
    def shows():

        now = datetime.now()

        upcoming = Shows.query.filter(Shows.date >= now).order_by(Shows.date.asc()).all()
        past = Shows.query.filter(Shows.date < now).order_by(Shows.date.asc()).all()
        
        return render_template('public/shows.html', upcoming=upcoming, past=past)
    
    @app.route('/contact')
    def contact():
        return render_template('public/contact.html')
    
    @app.route('/music')
    def music():

        return render_template('public/music.html')
    
    @app.route('/merch')
    def merch():

        merch = Merch.query.all()

        return render_template('public/merch.html', merch=merch)
    
    @app.route('/lessons')
    def lessons():
        return render_template('public/lessons.html')
    
    @app.route('/video')
    def video():
        return render_template('public/video.html')