from app import app, db
from models import User

def create_admin_user():
    with app.app_context():
        admin = User(username='ramilla')
        admin.set_password('123')
        admin.is_admin = True
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully!")

if __name__ == '__main__':
    create_admin_user()