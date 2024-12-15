from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

task_user = db.Table('task_user',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, nullable=True)
    completed_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    completed_by = db.relationship('User', foreign_keys=[completed_by_id], backref='completed_tasks')
    assigned_users = db.relationship('User', secondary=task_user, backref=db.backref('assigned_tasks', lazy=True))
