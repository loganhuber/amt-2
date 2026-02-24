from flask_sqlalchemy import SQLAlchemy
from flask import render_template, redirect, url_for, request, flash
from models import Shows, Merch
from datetime import datetime
from email_utils import build_email, send_email, EmailSendError




def register_routes(app):
    
    @app.route("/")
    def index():
        now = datetime.now()
        upcoming = Shows.query.filter(Shows.date >= now).order_by(Shows.date.asc()).all()

        return render_template('public/index.html', upcoming=upcoming)
    

    @app.route('/shows')
    def shows():

        now = datetime.now()

        upcoming = Shows.query.filter(Shows.date >= now).order_by(Shows.date.asc()).all()
        past = Shows.query.filter(Shows.date < now).order_by(Shows.date.asc()).all()
        
        return render_template('public/shows.html', upcoming=upcoming, past=past)
    
    @app.route('/contact', methods=["GET", "POST"])
    def contact():

        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')

            try:
                msg = build_email(email, name, message)
                send_email(msg)
                flash('Message received, we will reach out shortly!', 'success')
            except EmailSendError:
                flash("There was an error sending your message.")

            return redirect(url_for('index'))
            
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