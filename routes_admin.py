from flask_sqlalchemy import SQLAlchemy
from flask import render_template, redirect, url_for


def register_admin_routes(app):

    @app.route('/dashboard')
    def dashboard():
        render_template('admin/dashboard.html')


    @app.route('/login')
    def login():
        render_template('admin/login')

    
