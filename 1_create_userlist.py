from flask import Flask
from database import db
import random
import string
from models import User

def generate_password():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(12))

def create_admin_user(output_file):
    """Create admin user"""
    admin_user = User.query.filter_by(username='rln_admin').first()
    if admin_user:
        message = 'Admin user already exists'
        print(message)
        output_file.write(message + '\n')
        return

    admin_password = generate_password()
    admin_user = User(username='rln_admin', is_admin=True)
    admin_user.set_password(admin_password)
    db.session.add(admin_user)
    db.session.commit()
    message = f'Successfully created admin user with password: {admin_password}'
    print(message)
    output_file.write(message + '\n')

def create_test_users(output_file):
    """Create test users"""
    test_users = [
        {'username': 'Ramil'},
        {'username': 'Fatima'},
        {'username': 'Narmin'},
        {'username': 'Nurlan'}
    ]

    for user_data in test_users:
        user = User.query.filter_by(username=user_data['username']).first()
        if user:
            message = f"User {user_data['username']} already exists"
            print(message)
            output_file.write(message + '\n')
            continue

        password = generate_password()
        new_user = User(username=user_data['username'])
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        message = f"Created user {user_data['username']} with password: {password}"
        print(message)
        output_file.write(message + '\n')

def init_db():
    """Initialize database and create all users"""
    with app.app_context():
        db.create_all()
        with open('user_creation_results.txt', 'w') as output_file:
            create_admin_user(output_file)
            create_test_users(output_file)

if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    db.init_app(app)
    init_db()
