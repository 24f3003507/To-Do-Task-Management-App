from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create database object globally
db = SQLAlchemy() 

def create_app(): #factory function to create and configure the Flask app object and return it to be used in run.py
    app = Flask(__name__) #create Flask app instance

    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #initialize or link database with app
    db.__init__(app)

    from app.models import Task 
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app


