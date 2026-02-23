from flask_sqlalchemy import SQLAlchemy
from flask import render_template, redirect, url_for



def register_routes(app):
    
    @app.route("/")
    def index():
        return render_template('public/index.html')
    

    @app.route('/shows')
    def shows():
        return render_template('public/shows.html')
    
    @app.route('/contact')
    def contact():
        return render_template('public/contact.html')
    
    @app.route('/music')
    def music():

        return render_template('public/music.html')
    
    @app.route('/merch')
    def merch():
        return render_template('public/merch.html')
    
    @app.route('/lessons')
    def lessons():
        return render_template('public/lessons.html')
    
    @app.route('/video')
    def video():
        return render_template('public/video.html')