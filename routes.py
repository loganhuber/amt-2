from flask_sqlalchemy import SQLAlchemy
from flask import render_template, redirect, url_for, request, flash, send_from_directory
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from models import Shows, Merch, Admins
from datetime import datetime
from email_utils import build_email, send_email, EmailSendError
import os


def display_portal_link():
    if current_user.is_authenticated:
        flash("logged_in" "auth")



def register_routes(app):
    
    @app.route("/")
    def index():

        display_portal_link()

        now = datetime.now()
        upcoming = Shows.query.filter(Shows.date >= now).order_by(Shows.date.asc()).all()

        return render_template('public/index.html', upcoming=upcoming)
    

    @app.route('/shows')
    def shows():

        now = datetime.now()

        upcoming = Shows.query.filter(Shows.date >= now).order_by(Shows.date.asc()).all()
        past = Shows.query.filter(Shows.date < now).order_by(Shows.date.desc()).all()
        
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
    
    @app.route('/login', methods=["POST", "GET"])
    def login():

        if current_user.is_authenticated:
            return redirect(url_for('admin.index'))

        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            user = Admins.query.filter_by(username=username).first()

            if user and check_password_hash(user.pw_hash, password):
                login_user(user)
                return redirect('/admin')

            flash("Invalid Credentials")
        return render_template('admin/login.html')
    
    @app.route('/logout', methods=["GET", "POST"])
    def logout():

    
        logout_user()
        return redirect('/')
    
    @app.route('/uploads/<path:filename>')
    def uploaded_file(filename):
        return send_from_directory(
            os.path.join(app.instance_path, 'uploads'),
            filename
        )
